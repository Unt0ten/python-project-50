from gendiff import internal_representation_tree as get
import json
import pytest

@pytest.fixture
def node():
    return {'name': 'key', 'value': 'foo', 'status': 'unused'}


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
    file1 = json.load(open('tests/fixtures/file1_nested.json'))
    file2 = json.load(open('tests/fixtures/file2_nested.json'))
    result = [{'name': 'common',
               'value': [{'name': 'follow', 'value': False, 'status': 'added'},
                         {'name': 'setting1', 'value': 'Value 1',
                          'status': 'unchanged'},
                         {'name': 'setting2', 'value': 200,
                          'status': 'deleted'},
                         {'name': 'setting3', 'value': True,
                          'status': 'upd_del'},
                         {'name': 'setting3', 'value': None,
                          'status': 'upd_add'},
                         {'name': 'setting4', 'value': 'blah blah',
                          'status': 'added'},
                         {'name': 'setting5', 'value': {'key5': 'value5'},
                          'status': 'added'}, {'name': 'setting6', 'value': [
                       {'name': 'doge', 'value': [
                           {'name': 'wow', 'value': '', 'status': 'upd_del'},
                           {'name': 'wow', 'value': 'so much',
                            'status': 'upd_add'}], 'status': 'changed'},
                       {'name': 'key', 'value': 'value',
                        'status': 'unchanged'},
                       {'name': 'ops', 'value': 'vops', 'status': 'added'}],
                                               'status': 'changed'}],
               'status': 'changed'}, {'name': 'group1', 'value': [
        {'name': 'baz', 'value': 'bas', 'status': 'upd_del'},
        {'name': 'baz', 'value': 'bars', 'status': 'upd_add'},
        {'name': 'foo', 'value': 'bar', 'status': 'unchanged'},
        {'name': 'nest', 'value': {'key': 'value'}, 'status': 'upd_del'},
        {'name': 'nest', 'value': 'str', 'status': 'upd_add'}],
                                      'status': 'changed'},
              {'name': 'group2', 'value': {'abc': 12345, 'deep': {'id': 45}},
               'status': 'deleted'}, {'name': 'group3',
                                      'value': {'deep': {'id': {'number': 45}},
                                                'fee': 100500},
                                      'status': 'added'}]

    assert get.get_diff_data(file1, file2) == result


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
