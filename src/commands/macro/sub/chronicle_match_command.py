import typer
from datetime import datetime
from typing import Optional
from rich.console import Console
from config import settings

from src.pipeline.observers.handlers import PipelineStartLogHandler, \
    StepEnterLogHandler, StepTimeoutLogHandler, PipelineEndLogHandler, \
    PipelineResetLogHandler

from src.logging import LoggerConfig, LoggerFactory
from src.pipeline.observers import PipelineLogger
from src.macro.steps.chronicle_match import CHRONICLE_MATCH_STEPS
from src.pipeline.core import Pipeline, Step


console = Console()
app = typer.Typer(help=settings.TYPER.CHRONICLE_MATCH.help)

@app.command('chronicle-match', help=settings.TYPER.CHRONICLE_MATCH.help)
def chronicle_match_command(
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
    console.rule(settings.CLI.CHRONICLE_MATCH.rule)
    
    try:
        chronicle_match(max_loops, enable_log)
    except Exception:
        console.print(settings.CLI.CHRONICLE_MATCH.failed)
        console.print_exception(show_locals=True)


def chronicle_match(
    max_loops: Optional[int],
    enable_log: bool = True
):
    steps = [
        Step.from_spec(spec) for spec in CHRONICLE_MATCH_STEPS
    ]

    pipeline = Pipeline(
        steps,
        max_loops=max_loops
    )
    
    if enable_log:
        pipeline.add_observer(
            PipelineLogger(
                logger=LoggerFactory.get_logger(
                    config=LoggerConfig(
                        log_filename=f'{datetime.now().strftime("%H-%M-%S")}'
                    )
                ),
                handlers=(
                    PipelineEndLogHandler(),
                    PipelineStartLogHandler(),
                    StepEnterLogHandler(),
                    StepTimeoutLogHandler(),
                    PipelineResetLogHandler()
                )
            )
        )
    
    pipeline.run()
