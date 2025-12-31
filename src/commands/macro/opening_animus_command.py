import typer
from rich.console import Console
from config import settings

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
    max_loops: int | None = typer.Option(
        None,
        '--max-loops',
        help=settings.TYPER.OPENING_ANIMUS.max_loops_help
    )
):
    console.rule(settings.CLI.OPENING_ANIMUS.rule)
    
    try:
        criteria = load_passive_criteria_from_path(passive_criteria_path)
        opening_animus(max_loops, criteria)
    except Exception:
        console.print(settings.CLI.OPENING_ANIMUS.failed)
        console.print_exception(show_locals=True)


def opening_animus(
    max_loops: int | None,
    criteria: PassiveCriteria
):
    passives = load_passives(
        player_type=criteria.player_type,
        language=criteria.language
    )
    
    steps = [
        Step.from_spec(spec) for spec in OPENING_ANIMUS_STEPS
    ]

    pipeline = Pipeline(
        steps,
        max_loops=max_loops,
        context_data={
            'passives': passives,
            'criteria': criteria
        },
    )
    pipeline.run()
