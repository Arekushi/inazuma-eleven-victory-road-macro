import typer

from config import settings
from .sub.chronicle_match_command import chronicle_match_command
from .sub.opening_animus_command import opening_animus_command


app = typer.Typer(
    help=settings.TYPER.MACRO.help
)

app.command(
    'chronicle-match',
    help=settings.TYPER.CHRONICLE_MATCH.help
)(chronicle_match_command)

app.command(
    'opening-animus',
    help=settings.TYPER.OPENING_ANIMUS.help
)(opening_animus_command)
