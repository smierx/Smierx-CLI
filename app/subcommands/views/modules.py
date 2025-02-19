import frontmatter
import typer
from app.helper.prints import pprint, pprint_table
from app.core.config import settings
import os
import json
app = typer.Typer()


@app.command("all-modules")
def table_all_modules():
    modules = [x for x in os.listdir(f"{settings.BASE_PATH}/{settings.MODULE_PATH}") if x.endswith(".md")]
    tmp_data = []
    for module in modules:
        tmp_path = f"{settings.BASE_PATH}/{settings.MODULE_PATH}/{module}"
        with open(tmp_path,"r",encoding="utf-8") as f:
            data = frontmatter.load(f)

        pprint(json.dumps(data.metadata,indent=4))
        tmp_data.append(data.metadata)
    payload = [{
        "Identifier": x["Identifier"],
        "Name": x["Name"],
        "Semester": x["Semester"],
        "Exam Format": x["ExamFormat"] if "ExamFormat" in x else "N.K.",
        "NumSubModules": len(x["submodules_identifier"]) if "submodules_identifier" in x else 0,
        "NumPeriods":len(x["periods_identifier"]) if "periods_identifier" in x else 0,
    } for x in tmp_data]
    pprint_table(payload)