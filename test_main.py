from typer.testing import CliRunner
from main import app
from app.subcommands import helper
import pytest
import os

runner = CliRunner()

def test_main():
    result = runner.invoke(app,["--help"])
    assert result.exit_code == 0

def test_helper_get_lectures():
    result = helper.get_lectures()
    assert type(result) == list
    assert all(isinstance(n,str) for n in result)
    assert all(os.path.exists(n) for n in result)

def test_helper_get_lecture_titles():
    result = helper.get_lecture_titles()
    assert type(result) == list
    assert all(isinstance(n,str) for n in result)



def test_helper_lecture_titles_and_token():
    result = helper.get_lecture_titles_and_token()
    assert type(result) == list
    assert len(result) == 2
    assert all(isinstance(n,str) for n in result[0])
    assert all(isinstance(n,str) for n in result[1])

def test_helper_check_lectures():
    result = helper.check_lectures()
    assert result == True


@pytest.mark.parametrize(
    "lec_tok",[
        ("KE1"),
        ("KE2"),
        ("Test"),
    ]
)
def test_check_lecture_or_token(lec_tok:str):
    controll_result = helper.get_lecture_titles_and_token()
    result = helper.check_lecture_or_token(lec_tok)
    if lec_tok in controll_result[0] or lec_tok in controll_result[1]:
        assert result != ""
    if lec_tok in controll_result[0]:
        assert result != lec_tok

def test_lecture_find_lecture():
    pass