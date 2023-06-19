from gendiff.stylish import stylish


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_stylish():
    tree_flat = [
        {'name': 'follow', 'value': False, 'status': 'deleted', 'type': 'leaf'},
        {'name': 'host', 'value': 'hexlet.io', 'status': 'unchanged',
         'type': 'leaf'},
        {'name': 'proxy', 'value': '123.234.53.22', 'status': 'deleted',
         'type': 'leaf'},
        {'name': 'timeout', 'value': 50, 'status': 'deleted', 'type': 'leaf'},
        {'name': 'timeout', 'value': 20, 'status': 'added', 'type': 'leaf'},
        {'name': 'verbose', 'value': True, 'status': 'added', 'type': 'leaf'}]

    tree_nested = [{'name': 'common', 'children': [
        {'name': 'follow', 'value': False, 'status': 'added', 'type': 'leaf'},
        {'name': 'setting3', 'value': True, 'status': 'deleted',
         'type': 'leaf'},
        {'name': 'setting3', 'value': None, 'status': 'added', 'type': 'leaf'},
        {'name': 'setting6', 'children': [{'name': 'doge', 'children': [
            {'name': 'wow', 'value': '', 'status': 'deleted', 'type': 'leaf'},
            {'name': 'wow', 'value': 'so much', 'status': 'added',
             'type': 'leaf'}], 'status': 'changed', 'type': 'directory'},
                                          {'name': 'key', 'value': 'value',
                                           'status': 'unchanged',
                                           'type': 'leaf'}],
         'status': 'changed', 'type': 'directory'}], 'status': 'changed',
                    'type': 'directory'}, {'name': 'group1', 'children': [
        {'name': 'nest', 'children': [
            {'name': 'key', 'value': 'value', 'status': 'unused',
             'type': 'leaf'}], 'status': 'unused', 'type': 'directory'}],
                                           'status': 'deleted',
                                           'type': 'directory'},
                   {'name': 'group3', 'children': [
                       {'name': 'deep', 'value': [], 'status': 'unused',
                        'type': 'leaf'}], 'status': 'added',
                    'type': 'directory'}]

    assert stylish(tree_nested) == read('tests/fixtures/result_stylish')
    assert stylish(tree_flat) == read('tests/fixtures/result_flat_json_files')
