from gendiff import parser_files


def test_parser_files_json():
    file = 'tests/fixtures/file1.json'
    result = {"host": "hexlet.io", "timeout": 50,
              "proxy": "123.234.53.22",
              "follow": False}

    assert parser_files(file) == result


def test_parser_files_yaml():
    file = 'tests/fixtures/file1.yaml'
    result = {'author': 'Charles R. Saunders', 'language': 'English',
              'publication-year': 1981,
              'pages': 224}

    assert parser_files(file) == result


def test_parser_files_yml():
    file = 'tests/fixtures/file.yml'
    result = {'author': 'Charles R. Saunders', 'language': 'English',
              'publication-year': 1981,
              'pages': 224}

    assert parser_files(file) == result
