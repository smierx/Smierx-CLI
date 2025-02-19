import typer
from app.subcommands import config_router,view_router


app = typer.Typer()

app.add_typer(config_router.app, name="config")
app.add_typer(view_router.app, name="view")


if __name__=="__main__":
    app()
