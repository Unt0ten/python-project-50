from gendiff import formate_files


def test_formate_files_json():
    file = 'tests/fixtures/file1.json'
    result = {"host": "hexlet.io", "timeout": 50,
              "proxy": "123.234.53.22",
              "follow": False}

    assert formate_files(file) == result


def test_formate_files_yaml():
    file = 'tests/fixtures/file1.yaml'
    result = {'author': 'Charles R. Saunders', 'language': 'English',
              'publication-year': 1981,
              'pages': 224}

    assert formate_files(file) == result


def test_formate_files_yml():
    file = 'tests/fixtures/file.yml'
    result = {'author': 'Charles R. Saunders', 'language': 'English',
              'publication-year': 1981,
              'pages': 224}

    assert formate_files(file) == result
