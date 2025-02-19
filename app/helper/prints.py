from rich import print as rprint
from rich.console import Console
from rich.table import Table
import os
def pprint(payload:any):
    rprint(payload)

def pprint_table(payload:list[dict]):
    table = Table(show_header=True, header_style="bold magenta",expand=True)

    for column in payload[0].keys():
        table.add_column(column, style="cyan",justify="center")

    for row in payload:
        table.add_row(*[str(row[col]) for col in row])

    console = Console()
    os.system("cls" if os.name == "nt" else "clear")
    console.print(table)