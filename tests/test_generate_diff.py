from gendiff import generate_diff, to_string, format_value

FILE1 = {"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22",
         "follow": False}
FILE2 = {"timeout": 20, "verbose": True, "host": "hexlet.io"}


def test_generate_diff():
    string = (f'{{\n'
              f'  - follow: false\n'
              f'    host: hexlet.io\n'
              f'  - proxy: 123.234.53.22\n'
              f'  - timeout: 50\n'
              f'  + timeout: 20\n'
              f'  + verbose: true\n'
              f'}}')
    assert generate_diff(FILE1, FILE2) == string


def test_to_string():
    string = (f'{{\n'
              f'  foo: bar\n'
              f'  feez: baaz\n'
              f'}}')
    assert to_string({'foo': 'bar', 'feez': 'baaz'}) == string
    assert to_string({}) == (f'{{\n'
                             f'}}')


def test_format_value():
    assert format_value(True) == 'true'
    assert format_value(None) == 'null'
    assert format_value('foo') == 'foo'
