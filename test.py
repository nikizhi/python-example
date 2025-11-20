import pytest, os

def test_file():
    assert os.path.isfile('app.py') == True

