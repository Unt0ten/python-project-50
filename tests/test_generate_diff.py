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
