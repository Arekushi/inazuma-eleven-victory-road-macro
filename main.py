import typer
from src.commands.macro.macro import app as macro_app


def main():
    app = typer.Typer()
    app.add_typer(macro_app, name='macro')

    app()


if __name__ == '__main__':
    main()
