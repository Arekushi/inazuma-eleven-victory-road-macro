import typer
import src.commands.macro.macro as macro


def main():
    app = typer.Typer()
    app.add_typer(macro.app, name='macro')

    app()


if __name__ == '__main__':
    main()
