from gendiff.internal_representation_tree import gen_tree
from gendiff.generate_diff import generate_diff
import json


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_generate_diff():
    assert generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json') == read(
        'tests/fixtures/result_flat_json_files')

    assert generate_diff('tests/fixtures/file1_nested.json',
                         'tests/fixtures/file2_nested.json') == read(
        'tests/fixtures/result_nested_files_json')

    assert generate_diff('tests/fixtures/file1_nested.yaml',
                         'tests/fixtures/file2_nested.yaml') == read(
        'tests/fixtures/result_nested_files_yaml')


def test_gen_tree():
    file = json.load(open('tests/fixtures/file_for_gen_tree.json'))
    result = [{'name': 'common', 'children': [
        {'name': 'setting1', 'value': 'Value 1', 'status': 'unused',
         'type': 'leaf'},
        {'name': 'setting2', 'value': 200, 'status': 'unused', 'type': 'leaf'},
        {'name': 'setting3', 'value': True, 'status': 'unused', 'type': 'leaf'},
        {'name': 'setting6', 'children': [
            {'name': 'key', 'value': 'value', 'status': 'unused',
             'type': 'leaf'}, {'name': 'doge', 'children': [
                {'name': 'wow', 'value': '', 'status': 'unused',
                 'type': 'leaf'}], 'status': 'unused', 'type': 'directory'}],
         'status': 'unused', 'type': 'directory'}], 'status': 'unused',
               'type': 'directory'}]

    assert gen_tree(file) == result
