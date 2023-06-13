from gendiff import generate_diff

FILE1 = 'tests/fixtures/file1.json'
FILE2 = 'tests/fixtures/file2.json'


def test_generate_diff():
    string = (f'{{\n'
              f' - follow: false\n'
              f'   host: hexlet.io\n'
              f' - proxy: 123.234.53.22\n'
              f' - timeout: 50\n'
              f' + timeout: 20\n'
              f' + verbose: true\n'
              f'}}')
    assert generate_diff(FILE1, FILE2) == string
