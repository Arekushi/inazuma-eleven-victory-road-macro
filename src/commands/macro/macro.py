import typer

from config import settings
from .chronicle_match_command import chronicle_match_command


app = typer.Typer(
    help=settings.TYPER.MACRO.help
)

app.command(
    'chronicle-match',
    help=settings.TYPER.CHRONICLE_MATCH.help
)(chronicle_match_command)
