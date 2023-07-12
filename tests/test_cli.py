from gendiff.cli import parse_args
import pytest
import sys
import os


@pytest.fixture
def get_data():
    first_file = 'tests/fixtures/file1_nested.json'
    second_file = 'tests/fixtures/file2_nested.json'
    format = 'stylish'
    return first_file, second_file, format


def test_parse_args_first_file(get_data):
    first_file, second_file, format = get_data
    sys.argv = [
        'gendiff',
        first_file,
        second_file,
        '-f',
        format]
    args = parse_args()
    assert args.first_file == first_file


def test_parse_args_second_file(get_data):
    first_file, second_file, format = get_data
    sys.argv = [
        'gendiff',
        first_file,
        second_file,
        '-f',
        format]
    args = parse_args()
    assert args.second_file == second_file


def test_parse_args_format(get_data):
    first_file, second_file, format = get_data
    sys.argv = [
        'gendiff',
        first_file,
        second_file,
        '-f',
        format]
    args = parse_args()
    assert args.format == format


def test_cli_launch():
    command = os.system('poetry run gendiff -h')
    assert command == 0
