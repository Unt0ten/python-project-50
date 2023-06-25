from gendiff.formatters.stylish_module import stylish, get_nesting_depth
from gendiff.formatters.stylish_module import make_new_node_name
from gendiff.formatters.stylish_module import make_inner
from gendiff.formatters.format_value_module import format_value
from gendiff.formatters.plain_module import plain
from gendiff.formatters.plain_module import check_complex
from gendiff.formatters.plain_module import get_value_updated
from gendiff.formatters.plain_module import set_quotes
from gendiff.formatters.plain_module import convert_value
from gendiff.formatters.plain_module import make_string_flat
from gendiff.formatters.plain_module import make_string_nested
from gendiff.formatters.json_module import make_json
from gendiff.formatters.formater import apply_format
import pytest
import json


@pytest.fixture
def flat():
    return [
        {'name': 'follow', 'value': False, 'status': 'deleted'},
        {'name': 'host', 'value': 'hexlet.io', 'status': 'unchanged'},
        {'name': 'proxy', 'value': '123.234.53.22', 'status': 'deleted'},
        {'name': 'timeout', 'value': 50, 'status': 'upd_del'},
        {'name': 'timeout', 'value': 20, 'status': 'upd_add'},
        {'name': 'verbose', 'value': True, 'status': 'added'}]


@pytest.fixture
def nested():
    result = "tests/fixtures/result_get_diff_data_trees.json"
    with open(result, "r") as result:
        diff_result = json.load(result)
        return diff_result


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_make_new_node_name():
    assert make_new_node_name('key', 'changed') == '  key'
    assert make_new_node_name('key', 'deleted') == '- key'
    assert make_new_node_name('key', 'added') == '+ key'
    assert make_new_node_name('key', 'unused') == 'key'
    assert make_new_node_name('key', 'upd_add') == '+ key'
    assert make_new_node_name('key', 'upd_del') == '- key'


def test_get_nesting_depth():
    assert get_nesting_depth(1, 'unused') == 4
    assert get_nesting_depth(1, 'added') == 2


def test_format_value():
    assert format_value(True) == 'true'
    assert format_value(None) == 'null'
    assert format_value('foo') == 'foo'


def test_make_inner():
    value_dict = {'deep': {'id': {'number': 45}}, 'fee': 100500}
    value_list = [{'deep': {'id': {'number': 45}}, 'fee': 100500}]
    result = "tests/fixtures/result_make_inner.json"
    with open(result, "r") as result:
        result = json.load(result)
        assert make_inner(value_dict) == result

    assert make_inner(value_list) == value_list
    assert make_inner('foo') == 'foo'


def test_stylish(nested, flat):
    assert stylish(nested) == read('tests/fixtures/result_stylish')
    assert stylish(flat) == read('tests/fixtures/result_flat_json_files')


def test_check_complex():
    data1 = ['asd', 'qwerty']
    data2 = {'foo': 'bar'}
    data3 = 'baz'

    assert check_complex(data1) == '[complex value]'
    assert check_complex(data2) == '[complex value]'
    assert check_complex(data3) == 'baz'


def test_get_value_updated():
    node1 = {'name': 'setting3', 'value': True, 'status': 'upd_del'}
    node2 = {'name': 'setting3', 'value': None, 'status': 'upd_add'}

    assert get_value_updated(node1, 'upd_del') == 'true'
    assert get_value_updated(node2, 'upd_add') == 'null'


def test_set_quotes():
    assert set_quotes('true') == 'true'
    assert set_quotes('false') == 'false'
    assert set_quotes('null') == 'null'
    assert set_quotes('[complex value]') == '[complex value]'
    assert set_quotes(10) == 10
    assert set_quotes('fiz') == "'fiz'"


def test_convert_value():
    assert convert_value({'fiz': 'baz'}) == '[complex value]'
    assert convert_value(['fiz', 'baz']) == '[complex value]'
    assert convert_value(10) == 10
    assert convert_value(False) == 'false'
    assert convert_value('asd') == "'asd'"
    assert convert_value(None) == 'null'


def test_make_string_flat():
    assert make_string_flat(['group1'], 'asd',
                            'deleted') == "Property 'group1' was removed" + "\n"
    assert make_string_flat(['common', 'follow'], False,
                            'added') == \
           "Property 'common.follow' was added with value: false" + "\n"


def test_make_string_nested():
    node_del = {'name': 'setting3', 'value': True, 'status': 'upd_del'}
    node_add = {'name': 'setting3', 'value': None, 'status': 'upd_add'}
    assert make_string_nested(['common', 'setting3'], node_del,
                              'upd_del') == \
           "Property 'common.setting3' was updated. From true"
    assert make_string_nested(['common', 'setting3'], node_add,
                              'upd_add') == " to null" + "\n"


def test_plain(nested, flat):
    assert plain(flat) == read('tests/fixtures/result_plain_flat')
    assert plain(nested) == read('tests/fixtures/result_plain_nested')


def test_make_json(nested, flat):
    result_nested = make_json(nested)
    result_flat = make_json(flat)
    assert result_nested == read('tests/fixtures/result_to_json_nested.txt')
    assert result_flat == read('tests/fixtures/result_to_json_flat.txt')


def test_apply_format(nested):
    assert apply_format(nested, 'stylish') == read(
        'tests/fixtures/result_stylish')
    assert apply_format(nested, 'plain') == read(
        'tests/fixtures/result_plain_nested')
    assert apply_format(nested, 'json') == read(
        'tests/fixtures/result_to_json_nested.txt')
