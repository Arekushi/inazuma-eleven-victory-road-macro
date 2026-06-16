import typer
from typing import Optional
from rich.console import Console
from config import settings

from src.input.enums import InputMode
from src.application.match import MatchConfig, MatchPipeline


console = Console()
app = typer.Typer(help=settings.TYPER.MATCH.help)


@app.command('match', help=settings.TYPER.MATCH.help)
def match_command(
    input_mode: InputMode = typer.Option(
        InputMode.DESKTOP,
        '--input',
        help=settings.TYPER.MACRO.input_mode_help,
    ),
    max_loops: Optional[int] = typer.Option(
        None,
        '--max-loops',
        help=settings.TYPER.MACRO.max_loops_help
    ),
    enable_log_file: bool = typer.Option(
        False,
        '--log',
        help=settings.TYPER.MACRO.enable_log_file_help
    )
):
    console.rule(settings.CLI.MATCH.rule)
    
    try:
        config = MatchConfig(
            input_mode=input_mode,
            max_loops=max_loops,
            enable_log_file=enable_log_file
        )
        match(config)
    except Exception:
        console.print(settings.CLI.MATCH.failed)
        console.print_exception(show_locals=True)


def match(config: MatchConfig):
    MatchPipeline(config).build().run()
