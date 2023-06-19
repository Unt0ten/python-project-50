from gendiff import internal_representation_tree as get
import json


def test_get_diff_data_flat_files():
    file1 = {"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22",
             "follow": False}
    file2 = {"timeout": 20, "verbose": True, "host": "hexlet.io"}
    dict_ = {'- follow': False, '==host': 'hexlet.io',
             '- proxy': '123.234.53.22', '- timeout': 50, '+ timeout': 20,
             '+ verbose': True}

    assert get.get_diff_data(file1, file2) == dict_


def test_get_diff_data_trees():
    file1 = json.load(open('tests/fixtures/file1_nested.json'))
    file2 = json.load(open('tests/fixtures/file2_nested.json'))
    result = {
        '  common': {'+ follow': False, '==setting1': 'Value 1',
                     '- setting2': 200,
                     '- setting3': True, '+ setting3': None,
                     '+ setting4': 'blah blah',
                     '+ setting5': {'key5': 'value5'},
                     '  setting6': {'  doge': {'- wow': '', '+ wow': 'so much'},
                                    '==key': 'value', '+ ops': 'vops'}},
        '  group1': {'- baz': 'bas', '+ baz': 'bars', '==foo': 'bar',
                     '- nest': {'key': 'value'}, '+ nest': 'str'},
        '- group2': {'abc': 12345, 'deep': {'id': 45}},
        '+ group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}

    assert get.get_diff_data(file1, file2) == result


def test_isdict():
    data1 = {'key': 'value'}
    data2 = []

    assert get.isdict(data2) is False
    assert get.isdict(data1) is True


def test_make_node():
    result_dict_flat = {'name': 'key', 'value': 'foo',
                        'status': 'unused', 'type': 'leaf'}
    node_nested = {'name': 'common', 'children': [
        {'name': 'setting1', 'value': 'Value 1', 'status': 'unused',
         'type': 'leaf'}], 'status': 'unused', 'type': 'directory'}

    assert get.make_node('key', 'foo') == result_dict_flat
    assert get.make_node('common', [
        {'name': 'setting1', 'value': 'Value 1', 'status': 'unused',
         'type': 'leaf'}]) == node_nested


def test_get_children():
    node = {'name': 'common', 'children': [
        {'name': 'setting1', 'value': 'Value 1', 'status': 'unused',
         'type': 'leaf'}], 'status': 'unused', 'type': 'directory'}

    assert get.get_children(node) == [
        {'name': 'setting1', 'value': 'Value 1', 'status': 'unused',
         'type': 'leaf'}]


def test_is_directory():
    node1 = {'name': 'common', 'children': [
        {'name': 'setting1', 'value': 'Value 1', 'status': 'unused',
         'type': 'leaf'}], 'status': 'unused', 'type': 'directory'}
    node2 = {'name': 'key', 'value': 'foo',
             'status': 'unused', 'type': 'leaf'}

    assert get.is_directory(node1) is True
    assert get.is_directory(node2) is False


def test_get_value():
    node = {'name': 'key', 'value': 'foo',
            'status': 'unused', 'type': 'leaf'}

    assert get.get_value(node) == 'foo'


def test_get_status():
    node = {'name': 'key', 'value': 'foo',
            'status': 'unused', 'type': 'leaf'}

    assert get.get_status(node) == 'unused'


def test_get_name():
    node = {'name': 'key', 'value': 'foo',
            'status': 'unused', 'type': 'leaf'}

    assert get.get_name(node) == 'key'


def test_determine_status_node():
    node1 = {'name': '  key', 'value': 'foo',
             'status': 'unused', 'type': 'leaf'}
    node2 = {'name': '- key', 'value': 'foo',
             'status': 'unused', 'type': 'leaf'}
    node3 = {'name': '+ key', 'value': 'foo',
             'status': 'unused', 'type': 'leaf'}
    node4 = {'name': '==key', 'value': 'foo',
             'status': 'unused', 'type': 'leaf'}
    node5 = {'name': 'key', 'value': 'foo',
             'status': 'unused', 'type': 'leaf'}

    get.determine_status_node(node1)
    assert node1 == {'name': 'key',
                     'value': 'foo',
                     'status': 'changed',
                     'type': 'leaf'}

    get.determine_status_node(node2)
    assert node2 == {'name': 'key', 'value': 'foo',
                     'status': 'deleted',
                     'type': 'leaf'}

    get.determine_status_node(node3)
    assert node3 == {'name': 'key', 'value': 'foo',
                     'status': 'added',
                     'type': 'leaf'}

    get.determine_status_node(node4)
    assert node4 == {'name': 'key', 'value': 'foo',
                     'status': 'unchanged',
                     'type': 'leaf'}

    get.determine_status_node(node5)
    assert node5 == {'name': 'key', 'value': 'foo',
                     'status': 'unused',
                     'type': 'leaf'}
