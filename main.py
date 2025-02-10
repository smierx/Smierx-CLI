import typer
from app.subcommands import lecture,anki


app = typer.Typer()
app.add_typer(lecture.app,name="lecture")
app.add_typer(anki.app,name="anki")    

if __name__=="__main__":
    app()
