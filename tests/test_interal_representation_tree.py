from gendiff import internal_representation_diff as get
import json
import pytest


@pytest.fixture
def node():
    return {'name': 'key', 'value': 'foo', 'status': 'unused'}


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_get_diff_data_flat_files():
    file1 = {"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22",
             "follow": False}
    file2 = {"timeout": 20, "verbose": True, "host": "hexlet.io"}
    dict_ = [{'name': 'follow', 'value': False, 'status': 'deleted'},
             {'name': 'host', 'value': 'hexlet.io', 'status': 'unchanged'},
             {'name': 'proxy', 'value': '123.234.53.22', 'status': 'deleted'},
             {'name': 'timeout', 'value': 50, 'status': 'upd_del'},
             {'name': 'timeout', 'value': 20, 'status': 'upd_add'},
             {'name': 'verbose', 'value': True, 'status': 'added'}]

    assert get.get_diff_data(file1, file2) == dict_


def test_get_diff_data_trees():
    file1 = 'tests/fixtures/file1_nested.json'
    file2 = 'tests/fixtures/file2_nested.json'
    result = "tests/fixtures/result_get_diff_data_trees.json"

    with open(result, "r") as result, \
            open(file1, "r") as content1, open(file2, "r") as content2:
        diff_result = json.load(result)
        assert get.get_diff_data(json.load(content1),
                                 json.load(content2)) == diff_result


def test_isdict(node):
    data1 = node
    data2 = []

    assert get.isdict(data2) is False
    assert get.isdict(data1) is True


def test_make_node(node):
    result = node

    assert get.make_node('key', 'foo') == result


def test_get_value(node):
    assert get.get_value(node) == 'foo'


def test_get_status(node):
    assert get.get_status(node) == 'unused'


def test_get_name(node):
    assert get.get_name(node) == 'key'
