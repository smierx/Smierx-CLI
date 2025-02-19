import typer
from app.core.config import settings
from app.helper.prints import pprint
from app.subcommands.views import modules
app = typer.Typer()

@app.command()
def version():
    pprint(settings.VERSION_VIEW)

app.add_typer(modules.app)