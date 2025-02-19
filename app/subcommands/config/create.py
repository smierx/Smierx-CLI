import typer
from app.subcommands.config import create_module
from app.subcommands.helper import prints
app = typer.Typer()

@app.command()
def create(
    module: bool = typer.Option(False, "--module","-m", help="Create a new Module"),
    period: bool = typer.Option(False, "--period","-p", help="Create a new period"),
    session: bool = typer.Option(False, "--session","-s", help="Create a new session"),
    keydate: bool = typer.Option(False, "--keydate","-k", help="Create a new keydate"),

    name: str = typer.Argument(None,  help="Name of the module"),
):
    selected_options = [module, period,session, keydate]
    if sum(selected_options) != 1:
        prints.pprint("You must select exactly one option: --module, --period,--session or --keydate.")
        raise typer.Exit()

    if module:
        if not name:
            prints.pprint("Error: --module requires a name as first argument.")
            raise typer.Exit()
        create_module.create()

