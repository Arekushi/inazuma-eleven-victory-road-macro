import typer
from typing import Optional
from rich.console import Console
from config import settings

from config.paths import Paths
from src.input.enums import InputMode
from src.application.match import MatchConfig, MatchPipeline
from src.commands.helpers import prompt_if_none, prompt_macro_name
from src.enums.language import Language


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
    input_mode: InputMode = typer.Option(
        InputMode.DESKTOP,
        '--input',
        help=settings.TYPER.MACRO.input_mode_help,
    ),
    language: Language = typer.Option(
        Language.PT_BR,
        '--language',
        help=settings.TYPER.MACRO.language_help
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
        config = MatchConfig(
            macro_path=Paths.macro(MACRO_SUB_FOLDER, macro_filename),
            input_mode=input_mode,
            max_loops=max_loops,
            language=language,
            enable_log=enable_log
        )
        match(config)
    except Exception:
        console.print(settings.CLI.MATCH.failed)
        console.print_exception(show_locals=True)


def match(config: MatchConfig):
    MatchPipeline(config).build().run()
