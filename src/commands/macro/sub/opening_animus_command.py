import typer
from datetime import datetime
from typing import Optional
from rich.console import Console
from config import settings

from src.pipeline.observers.handlers import PipelineStartLogHandler, \
    StepEnterLogHandler, PipelineEndLogHandler, OpeningAnimusTimeoutLogHandler, \
    PipelineResetLogHandler

from src.logging import LoggerFactory, LoggerConfig
from src.pipeline.observers import PipelineLogger
from src.macro.steps import OPENING_ANIMUS_STEPS
from src.passives.loaders import load_passive_criteria_from_path, load_passives
from src.passives.classes import PassiveCriteria
from src.pipeline.core import Pipeline, Step


console = Console()
app = typer.Typer(help=settings.TYPER.OPENING_ANIMUS.help)

@app.command('opening-animus', help=settings.TYPER.OPENING_ANIMUS.help)
def opening_animus_command(
    passive_criteria_path: str = typer.Option(
        ...,
        '--criteria',
        help=settings.TYPER.OPENING_ANIMUS.passive_criteria_path_help
    ),
    max_loops: Optional[int] = typer.Option(
        None,
        '--max-loops',
        help=settings.TYPER.MACRO.max_loops_help
    ),
    enable_log: bool = typer.Option(
        False,
        '--log',
        help=settings.TYPER.MACRO.enable_log_help
    )
):
    console.rule(settings.CLI.OPENING_ANIMUS.rule)
    
    try:
        criteria = load_passive_criteria_from_path(passive_criteria_path)
        opening_animus(max_loops, criteria, enable_log)
    except Exception:
        console.print(settings.CLI.OPENING_ANIMUS.failed)
        console.print_exception(show_locals=True)


def opening_animus(
    max_loops: Optional[int],
    criteria: PassiveCriteria,
    enable_log: bool = True
):
    passives = load_passives(
        player_type=criteria.player_type,
        language=criteria.language
    )
    
    steps = [
        Step.from_spec(spec) for spec in OPENING_ANIMUS_STEPS
    ]
    
    logger = LoggerFactory.get_logger(
        config=LoggerConfig(
            log_filename=f'{criteria.name}-{datetime.now().strftime("%H-%M-%S")}'
        )
    )

    pipeline = Pipeline(
        steps=steps,
        logger=logger,
        max_loops=max_loops,
        context_data={
            'passives': passives,
            'criteria': criteria
        },
    )
    
    if enable_log:
        pipeline.add_observer(
            PipelineLogger(
                logger=logger,
                handlers=(
                    PipelineEndLogHandler(),
                    PipelineStartLogHandler(),
                    StepEnterLogHandler(),
                    OpeningAnimusTimeoutLogHandler(),
                    PipelineResetLogHandler()
                )
            )
        )
    
    pipeline.run()
