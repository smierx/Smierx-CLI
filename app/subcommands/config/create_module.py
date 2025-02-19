from app.subcommands.helper import prints
from app.core.config import settings
import typer

def create():
    prints.pprint(settings.VERSION_CONFIG)

