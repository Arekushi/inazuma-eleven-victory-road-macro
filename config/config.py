from dynaconf import Dynaconf


settings = Dynaconf(
    settings_files=[
        './toml/typer.toml',
        './toml/cli.toml',
        './toml/settings.toml'
    ],
    load_dotenv=True,
    envvar_prefix=False
)
