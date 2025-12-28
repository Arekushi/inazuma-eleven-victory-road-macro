import typer
from rich.console import Console
from config import settings

from src.pipeline.pipeline import Pipeline
from src.pipeline.step import Step
from src.macros.chronicle_match import chronicle_match_steps


console = Console()
app = typer.Typer(help=settings.TYPER.CHRONICLE_MATCH.help)

@app.command('chronicle-match', help=settings.TYPER.CHRONICLE_MATCH.help)
def chronicle_match_command(
    max_loops: int | None = typer.Option(
        None,
        '--max-loops',
        help=settings.TYPER.CHRONICLE_MATCH.max_loops_help
    )
):
    console.rule(settings.CLI.CHRONICLE_MATCH.rule)
    
    try:
        chronicle_match(max_loops)
    except Exception:
        console.print(settings.CLI.CHRONICLE_MATCH.failed)
        console.print_exception(show_locals=True)


def chronicle_match(max_loops):
    steps = [
        Step.from_spec(spec) for spec in chronicle_match_steps
    ]

    pipeline = Pipeline(steps, max_loops=max_loops)
    pipeline.run()
