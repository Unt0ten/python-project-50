from gendiff.parser_files import get_data


def test_parser_files_json():
    file = 'tests/fixtures/file1.json'
    result = {"host": "hexlet.io", "timeout": 50,
              "proxy": "123.234.53.22",
              "follow": False}

    assert get_data(file) == result


def test_parser_files_yaml():
    file = 'tests/fixtures/file1.yaml'
    result = {'author': 'Charles R. Saunders', 'language': 'English',
              'publication-year': 1981,
              'pages': 224}

    assert get_data(file) == result


def test_parser_files_yml():
    file = 'tests/fixtures/file.yml'
    result = {'author': 'Charles R. Saunders', 'language': 'English',
              'publication-year': 1981,
              'pages': 224}

    assert get_data(file) == result
