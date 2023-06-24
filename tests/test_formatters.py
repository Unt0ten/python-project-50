from gendiff.formatters.stylish_module import stylish, get_nesting_depth
from gendiff.formatters.stylish_module import make_new_node_name
from gendiff.formatters.format_value_module import format_value


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_make_new_node_name():
    assert make_new_node_name('key', 'changed') == '  key'
    assert make_new_node_name('key', 'deleted') == '- key'
    assert make_new_node_name('key', 'added') == '+ key'
    assert make_new_node_name('key', 'unchanged') == '  key'
    assert make_new_node_name('key', 'unused') == 'key'


def test_get_nesting_depth():
    assert get_nesting_depth(1, 'unused') == 4
    assert get_nesting_depth(1, 'added') == 2


def test_format_value():
    assert format_value(True) == 'true'
    assert format_value(None) == 'null'
    assert format_value('foo') == 'foo'


def test_stylish():
    tree_flat = [
        {'name': 'follow', 'value': False, 'status': 'deleted'},
        {'name': 'host', 'value': 'hexlet.io', 'status': 'unchanged'},
        {'name': 'proxy', 'value': '123.234.53.22', 'status': 'deleted'},
        {'name': 'timeout', 'value': 50, 'status': 'deleted'},
        {'name': 'timeout', 'value': 20, 'status': 'added'},
        {'name': 'verbose', 'value': True, 'status': 'added'}]

    tree_nested = [{'name': 'common', 'value': [
        {'name': 'follow', 'value': False, 'status': 'added'},
        {'name': 'setting1', 'value': 'Value 1', 'status': 'unchanged'},
        {'name': 'setting2', 'value': 200, 'status': 'deleted'},
        {'name': 'setting3', 'value': True, 'status': 'upd_del'},
        {'name': 'setting3', 'value': None, 'status': 'upd_add'},
        {'name': 'setting4', 'value': 'blah blah', 'status': 'added'},
        {'name': 'setting5', 'value': {'key5': 'value5'}, 'status': 'added'},
        {'name': 'setting6', 'value': [{'name': 'doge', 'value': [
            {'name': 'wow', 'value': '', 'status': 'upd_del'},
            {'name': 'wow', 'value': 'so much', 'status': 'upd_add'}],
                                        'status': 'changed'},
                                       {'name': 'key', 'value': 'value',
                                        'status': 'unchanged'},
                                       {'name': 'ops', 'value': 'vops',
                                        'status': 'added'}],
         'status': 'changed'}], 'status': 'changed'},
                   {'name': 'group1', 'value': [
                       {'name': 'baz', 'value': 'bas', 'status': 'upd_del'},
                       {'name': 'baz',
                        'value': 'bars',
                        'status': 'upd_add'},
                       {'name': 'foo',
                        'value': 'bar',
                        'status': 'unchanged'},
                       {
                           'name': 'nest',
                           'value': {
                               'key': 'value'},
                           'status': 'upd_del'},
                       {
                           'name': 'nest',
                           'value': 'str',
                           'status': 'upd_add'}],
                    'status': 'changed'},
                   {'name': 'group2',
                    'value': {'abc': 12345, 'deep': {'id': 45}},
                    'status': 'deleted'}, {'name': 'group3', 'value': {
            'deep': {'id': {'number': 45}}, 'fee': 100500}, 'status': 'added'}]

    assert stylish(tree_nested) == read('tests/fixtures/result_stylish')
    assert stylish(tree_flat) == read('tests/fixtures/result_flat_json_files')
