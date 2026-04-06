import typer

from config import settings
from .sub.match_command import match_command


app = typer.Typer(
    help=settings.TYPER.MACRO.help
)

app.command(
    'match',
    help=settings.TYPER.MATCH.help
)(match_command)
