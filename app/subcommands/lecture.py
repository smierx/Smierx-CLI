import typer
import os
from app.subcommands import helper
from app.core.config import settings
import csv

import frontmatter
import datetime


app = typer.Typer()


@app.command()
def main(command: str,sure=False):
    if command=="test":
        print("Das ist der Test")
    elif command=="fix-lectures":
        if sure:
            for tmp_path in helper._get_lectures():
                with open(tmp_path,"r") as file:
                    tmp_data = frontmatter.load(file)

                tmp_data["token"] = ""

                with open(tmp_path,"w") as file:
                    file.write(frontmatter.dumps(tmp_data))
    else:
        print("hello world")

@app.command()
def find_lectures():
    for tmp_path in helper._get_lectures():
        print(tmp_path)



@app.command()
def checks():
    helper.check_lectures()


@app.command()
def create_lecture_csv(lecture: str, date=datetime.date.today().strftime("%Y-%m-%d"),subtitle="Subtitle"):
    helper.check_lectures()
    if (lecture :=helper._check_lecture_or_token(lecture)) == "":
        return
    with open(f"{settings.BASE_PATH}/{settings.TEMPLATE_REL_PATH}/{settings.TEMPLATE_CSV}","r") as file:
        reader = csv.reader(file,delimiter=";")
        rows = list(reader)
    tmp_data = []
    for row in rows:
        tmp_row = []
        if row[0]=="Lecture":
            tmp_row.append("Lecture")
            tmp_row.append(lecture)
        elif row[0] == "Date":
            tmp_row.append("Date")
            tmp_row.append(date)
        elif row[0] == "Subtitle":
            tmp_row.append(subtitle)
            tmp_row.append("")
            tmp_row.append("x")
        else:
            tmp_row = row
        tmp_data.append(tmp_row)

    counter = len([x for x in os.listdir(f"{settings.BASE_PATH}/{settings.TABLES_REL_PATH}/") if lecture in x])
    with open(f"{settings.BASE_PATH}/{settings.TABLES_REL_PATH}/{lecture}_{counter}.csv","w") as file:
        writer = csv.writer(file,delimiter=";")
        writer.writerows(tmp_data)

@app.command()
def transfer_csv_to_md(lecture: str):
    helper.check_lectures()
    if (lecture := helper._check_lecture_or_token(lecture)) == "":
        return

    files = [x for x in os.listdir(f"{settings.BASE_PATH}/{settings.TABLES_REL_PATH}/") if lecture in x]
    
    link_str = f"[[{settings.BASE_PATH}/{settings.LECTURE_REL_PATH}/{lecture}.md]]"
    
    for file in files:
        with open(f"{settings.BASE_PATH}/{settings.TABLES_REL_PATH}/{file}","r") as file:
            reader = csv.reader(file,delimiter=";")
            rows = list(reader)
        metadata = rows[0:settings.START_ROW]
        full_data = rows[settings.START_ROW:]
        
        question_dir = {}
        tmp_data = []
        title = None
        for x in full_data:
            if len(x)==3 and x[-1] == "x":
                if title != None:
                    question_dir[title] = tmp_data
                title = x[0]
                print(title)
                tmp_data = []
            elif x[0] != "":
                tmp_data.append((x[0],x[1]))
        question_dir[title] = tmp_data
        print(question_dir)



if __name__=="__main__":
    app()
