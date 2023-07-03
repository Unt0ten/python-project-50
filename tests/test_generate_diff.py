from gendiff.generate_diff import generate_diff
import pytest


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


@pytest.mark.parametrize("file_path1, file_path2, formatter, expected_result",
                         [
                             ('tests/fixtures/file1.json',
                              'tests/fixtures/file2.json',
                              'stylish',
                              'tests/fixtures/result_flat_json_files'),
                             ('tests/fixtures/file1_nested.json',
                              'tests/fixtures/file2_nested.json',
                              'stylish',
                              'tests/fixtures/result_nested_files_json'),
                             ('tests/fixtures/file1.json',
                              'tests/fixtures/file2.json',
                              'plain',
                              'tests/fixtures/result_plain_flat'),
                             ('tests/fixtures/file1_nested.json',
                              'tests/fixtures/file2_nested.json',
                              'plain',
                              'tests/fixtures/result_plain_nested'),
                             ('tests/fixtures/file1.yaml',
                              'tests/fixtures/file2.yaml',
                              'stylish',
                              'tests/fixtures/result_flat_yaml_files'),
                             ('tests/fixtures/file1_nested.yaml',
                              'tests/fixtures/file2_nested.yaml',
                              'stylish',
                              'tests/fixtures/result_nested_files_yaml'),
                             ('tests/fixtures/file1.yaml',
                              'tests/fixtures/file2.yaml',
                              'plain',
                              'tests/fixtures/result_yaml_flat_plain'),
                             ('tests/fixtures/file1_nested.yaml',
                              'tests/fixtures/file2_nested.yaml',
                              'plain',
                              'tests/fixtures/result_yaml_nested_plain'),
                             ('tests/fixtures/file1.json',
                              'tests/fixtures/file2.json',
                              'json',
                              'tests/fixtures/result_to_json_flat.txt'),
                             ('tests/fixtures/file.yml',
                              'tests/fixtures/file2.yml',
                              'stylish',
                              'tests/fixtures/result_flat_yaml_files')
                         ])
def test_generate_diff(file_path1, file_path2, formatter, expected_result):
    assert generate_diff(file_path1, file_path2, formatter) == read(
        expected_result)
