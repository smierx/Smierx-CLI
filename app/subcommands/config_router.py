import typer
from app.core.config import settings
from app.subcommands.helper.prints import pprint
from app.subcommands.config import create
app = typer.Typer()

@app.command()
def version():
    typer.echo(settings.VERSION_CONFIG)
    pprint(settings.VERSION_CONFIG)

app.add_typer(create.app)