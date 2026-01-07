import typer
from datetime import datetime
from typing import Optional
from rich.console import Console
from config import settings

from src.logging import LoggerFactory, LoggerConfig
from src.pipeline.observers.handlers import (
    PipelineStartLogHandler,
    StepEnterLogHandler,
    PipelineEndLogHandler,
    OpeningAnimusTimeoutLogHandler,
    PipelineResetLogHandler
)

from src.profiles.loaders import load_profile_by_name
from src.profiles.classes import Profile
from src.profiles.exceptions import PassiveCriteriaNotFoundException

from src.pipeline.observers import PipelineLogger

from src.passives.loaders import load_passives
from src.dsl.compiler import PipelineCompiler

from src.commands.helpers import (
    select_profile_name,
    select_passive_criteria
)


console = Console()
app = typer.Typer(help=settings.TYPER.OPENING_ANIMUS.help)

@app.command('opening-animus', help=settings.TYPER.OPENING_ANIMUS.help)
def opening_animus_command(
    profile_name: str = typer.Option(
        None,
        '--profile',
        help=settings.TYPER.MACRO.profile_name_help
    ),
    passive_criteria_name: str = typer.Option(
        None,
        '--criteria',
        help=settings.TYPER.OPENING_ANIMUS.passive_criteria_name_help
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
        if profile_name is None:
            profile_name = select_profile_name()

        profile = load_profile_by_name(profile_name)

        if not passive_criteria_name:
            passive_criteria_name = select_passive_criteria(profile.passive_criterias)
        elif passive_criteria_name not in profile.passive_criterias:
            raise PassiveCriteriaNotFoundException(
                passive_criteria_name,
                profile.name
            )
                
        opening_animus(
            profile,
            passive_criteria_name,
            max_loops,
            enable_log
        )
    except Exception:
        console.print(settings.CLI.OPENING_ANIMUS.failed)
        console.print_exception(show_locals=False)


def opening_animus(
    profile: Profile,
    passive_criteria_name: str,
    max_loops: Optional[int] = None,
    enable_log: bool = True
):
    criteria = profile.passive_criterias[passive_criteria_name]
    pipeline = PipelineCompiler.compile_file(profile.macros['opening-animus'].path)
    
    passives = load_passives(
        spirit_type=criteria.spirit.type,
        language=profile.language
    )
    
    logger = LoggerFactory.get_logger(
        config=LoggerConfig(
            name='opening-animus-command',
            log_filename=f'{criteria.spirit.name.lower()}-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S.%f")}'
        )
    )
    
    pipeline.max_loops = max_loops
    pipeline.context.update({
        'passives': passives,
        'criteria': criteria,
        'profile': profile
    })
    
    if enable_log:
        pipeline.logger = logger
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
