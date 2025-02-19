import typer
from app.subcommands.config import create_module
from app.helper import prints,ids
from app.schemas.modules import Module,Submodule

app = typer.Typer()


def get_valid_number(value: int,min_value:int, reason:str) -> int:
    if value < min_value:
        while True:
            value = typer.prompt(f"Enter number of {reason}: ", type=int)
            if value >= min_value:
                return value
            typer.echo(f"⚠️ Exception: The number has to be at least {min_value}!", err=True)
    return value


@app.command()
def create(
    module: bool = typer.Option(False, "--module","-m", help="Create a new Module"),
    period: bool = typer.Option(False, "--period","-p", help="Create a new period"),
    session: bool = typer.Option(False, "--session","-s", help="Create a new session"),
    keydate: bool = typer.Option(False, "--keydate","-k", help="Create a new keydate"),

    name: str = typer.Argument(None,  help="Name of the module"),
    number_of_submodules: int = typer.Option(None,"-n", help="Number of submodules"),
    timestamp: str = typer.Option(None,"-t",help="Earliest relevant timestamp. Format=%Y-%m-%d"),
    exam_format: bool = typer.Option(False,"-f",help="Exam format"),
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

