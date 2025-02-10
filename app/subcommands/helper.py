import frontmatter

from app.core.config import settings
import os

def _get_lectures():
    return [f"{settings.BASE_PATH}/{settings.LECTURE_REL_PATH}/{x}" for x in os.listdir(f"{settings.BASE_PATH}/{settings.LECTURE_REL_PATH}") if x.endswith(".md")]

def _get_lecture_titles():
    return [x.split("/")[-1].split(".md")[0] for x in _get_lectures()]

def _get_lecture_titles_and_token():
    data = []
    lectures = _get_lectures()
    files = []
    tokens = []
    for x in lectures:
        tmp_file_title = x.split("/")[-1].split(".md")[0]
        with open(x,"r") as file:
            tmp_data = frontmatter.load(file)
        tmp_token = tmp_data["token"]
        files.append(tmp_file_title)
        tokens.append(tmp_token)
    data.append(files)
    data.append(tokens)
    return data


def check_lectures():
    tokens = []
    for tmp_path in _get_lectures():
        with open(tmp_path,"r") as file:
            tmp_data = frontmatter.load(file)
        assert "Subject" in tmp_data.metadata, tmp_path.split("/")[-1]
        assert str(tmp_data["Subject"]).startswith("[["),tmp_path.split("/")[-1]
        assert str(tmp_data["Subject"]).endswith("]]"),tmp_path.split("/")[-1]
        if tmp_data["token"] != "":
            assert tmp_data["token"] not in tokens,tmp_path.split("/")[-1]
            tokens.append(str(tmp_data["token"]))
    print("Alle Tests erfolgreich!")



def _check_lecture_or_token(lec_tok:str):
    data = _get_lecture_titles_and_token()
    if (lec_tok not in data[0]) and (lec_tok not in data[1]):
        return ""
    flag = (0,1) if lec_tok in data[0] else (1,0)
    return lec_tok if flag[0] == 0 else data[flag[1]][data[flag[0]].index(lec_tok)]

