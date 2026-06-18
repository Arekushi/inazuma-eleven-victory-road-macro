poetry run pyinstaller `
  --noconfirm `
  --onedir `
  --console `
  --icon "assets/ie-vr-macro-icon.ico" `
  --name "ie-vr-macro" `
  --add-data "assets/end-second-half-validator.png;assets/." `
  --add-data "config/toml/cli.toml;config/toml/." `
  --add-data "config/toml/settings.toml;config/toml/." `
  --add-data "config/toml/typer.toml;config/toml/." `
  --add-data "macros/match.vml;macros/." `
  --add-data "repo/metadata;repo/metadata/." `
  --collect-binaries=vgamepad `
  main.py
