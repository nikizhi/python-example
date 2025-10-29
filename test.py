import pytest, os

def file_test():
    assert os.path.isfile('app.py') == True
