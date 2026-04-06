import typer
from pathlib import Path
from datetime import datetime
from typing import Optional
from rich.console import Console
from config import settings

from config.paths import Paths
from src.pipeline.observers.handlers import (
    PipelineStartLogHandler,
    StepEnterLogHandler,
    PipelineEndLogHandler,
    PipelineResetLogHandler,
    StepTimeoutLogHandler
)

from src.commands.helpers import prompt_if_none, prompt_macro_name
from src.enums.language import Language
from src.logging import LoggerConfig, LoggerFactory
from src.pipeline.observers import PipelineLogger
from src.dsl.compiler import PipelineCompiler


MACRO_SUB_FOLDER = 'match'
console = Console()
app = typer.Typer(help=settings.TYPER.MATCH.help)

@app.command('match', help=settings.TYPER.MATCH.help)
def match_command(
    macro_filename: str = typer.Option(
        None,
        '--file',
        help=settings.TYPER.MATCH.macro_file_help,
        callback=prompt_if_none(prompt_macro_name, MACRO_SUB_FOLDER)
    ),
    language: Language = typer.Option(
        Language.PT_BR,
        '--language',
        help=settings.TYPER.MACRO.language
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
    console.rule(settings.CLI.MATCH.rule)
    
    try:
        macro_path = Paths.macro(MACRO_SUB_FOLDER, macro_filename)
        match(macro_path, language, max_loops, enable_log)
    except Exception:
        console.print(settings.CLI.MATCH.failed)
        console.print_exception(show_locals=True)


def match(
    macro_path: Path,
    language: Language,
    max_loops: Optional[int],
    enable_log: bool = True
):
    pipeline = PipelineCompiler.compile_file(macro_path)
    pipeline.max_loops = max_loops
    pipeline.context.update({
        'language': language
    })
    
    if enable_log:
        logger = LoggerFactory.get_logger(
            config=LoggerConfig(
                name=f'{macro_path.stem}_command',
                log_filename=f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S.%f")}'
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
