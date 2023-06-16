from gendiff import format_value
from gendiff import get_diff_data
from fixtures import file1_test_generate_diff_trees
from fixtures import file2_test_generate_diff_trees
from fixtures import result_generate_diff_trees



def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_get_diff_data_flat_files():
    file1 = {"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22",
             "follow": False}
    file2 = {"timeout": 20, "verbose": True, "host": "hexlet.io"}
    dict_ = {'- follow': False, '  host': 'hexlet.io',
             '- proxy': '123.234.53.22', '- timeout': 50, '+ timeout': 20,
             '+ verbose': True}
    assert get_diff_data(file1, file2) == dict_


def test_get_diff_data_trees():
    file1 = file1_test_generate_diff_trees.dict_
    file2 = file2_test_generate_diff_trees.dict_
    result = result_generate_diff_trees.result

    assert get_diff_data(file1, file2) == result


def test_format_value():
    assert format_value(True) == 'true'
    assert format_value(None) == 'null'
    assert format_value('foo') == 'foo'
