import typer
from app.core.config import settings
from app.subcommands.helper.prints import pprint
from app.subcommands.config import create_module
app = typer.Typer()

@app.command()
def version():
    pprint(settings.VERSION_CONFIG)

app.add_typer(create_module.app)