import typer
from app.subcommands import config_router


app = typer.Typer()

app.add_typer(config_router.app, name="config")

if __name__=="__main__":
    app()
