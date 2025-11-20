import pytest, os

def test_file():
    assert os.path.exists('app.py'), "Не удалось найти файл app.py."


