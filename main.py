import typer
from app.subcommands import lecture,anki,notes


app = typer.Typer()
app.add_typer(lecture.app,name="lecture")
app.add_typer(anki.app,name="anki")    
app.add_typer(notes.app,name="notes")

if __name__=="__main__":
    app()
