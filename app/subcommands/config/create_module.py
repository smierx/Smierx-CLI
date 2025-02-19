from app.helper import prints
from app.schemas.modules import Module,Submodule
from app.core.config import settings
import typer

def create():
    prints.pprint(settings.VERSION_CONFIG)

