import typer
from datetime import datetime
from typing import Optional
from rich.console import Console
from config import settings

from src.pipeline.observers.handlers import (
    PipelineStartLogHandler,
    StepEnterLogHandler,
    PipelineEndLogHandler,
    PipelineResetLogHandler,
    StepTimeoutLogHandler
)

from src.profiles.classes import Profile
from src.profiles.loaders import load_profile_by_name

from src.commands.helpers import select_profile_name
from src.logging import LoggerConfig, LoggerFactory
from src.pipeline.observers import PipelineLogger
from src.dsl.compiler import PipelineCompiler


console = Console()
app = typer.Typer(help=settings.TYPER.CHRONICLE_MATCH.help)

@app.command('chronicle-match', help=settings.TYPER.CHRONICLE_MATCH.help)
def chronicle_match_command(
    profile_name: str = typer.Option(
        None,
        '--profile',
        help=settings.TYPER.MACRO.profile_name_help
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
    console.rule(settings.CLI.CHRONICLE_MATCH.rule)
    
    try:
        if profile_name is None:
            profile_name = select_profile_name()

        profile = load_profile_by_name(profile_name)
        
        chronicle_match(profile, max_loops, enable_log)
    except Exception:
        console.print(settings.CLI.CHRONICLE_MATCH.failed)
        console.print_exception(show_locals=True)


def chronicle_match(
    profile: Profile,
    max_loops: Optional[int],
    enable_log: bool = True
):
    pipeline = PipelineCompiler.compile_file(profile.macros['chronicle_match'].path)
    pipeline.max_loops = max_loops
    pipeline.context.update({
        'profile': profile
    })
    
    if enable_log:
        logger = LoggerFactory.get_logger(
            config=LoggerConfig(
                name='chronicle_match_command',
                log_filename=f'{profile.name.lower()}-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S.%f")}'
            )
        )
        
        pipeline.logger = logger
        pipeline.add_observer(
            PipelineLogger(
                logger=logger,
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
