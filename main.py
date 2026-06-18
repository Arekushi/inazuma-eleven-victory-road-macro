import typer

from src.commands.macro.macro import app as macro_app
from src.tufup.tufup_updater import TufupUpdater


app = typer.Typer()


@app.callback()
def main(
    ctx: typer.Context,
    no_update_check: bool = typer.Option(
        False,
        '--no-update-check'
    ),
):
    updater = TufupUpdater()
    
    if not no_update_check:
        update = updater.has_update()

        if update:
            typer.echo(f'\nNew version: {update.version}')
            updater.update()


app.add_typer(macro_app, name='macro')


if __name__ == '__main__':
    app()
