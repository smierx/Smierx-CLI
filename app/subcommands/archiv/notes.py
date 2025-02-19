import typer
from app.core.config import settings
import os
import datetime

app = typer.Typer()

@app.command()
def academic():
    today = datetime.date.today().strftime("%Y-%m-%d")
    with open(f"{settings.BASE_PATH}/Akademisches Notizbuch.md", "r") as file:
        data = file.readlines()

    new_data = []
    today_finished = False
    for line in data:
        if line.startswith("## ") and today in line:
            today_finished = True
        if line.startswith("## ") and not today_finished:
            new_data.append(f"## {today}\n\n")
        new_data.append(line)

    with open(f"{settings.BASE_PATH}/Akademisches Notizbuch.md","w") as file:
        file.writelines(new_data)