import json


def format_value(value):
    '''
    This function formats bool and Nonetype dictionary values from .py to .json.
    '''
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return value


def to_string(dict_):
    '''
    This function formats the dictionary into a string.
    '''
    string = ''
    for k, v in dict_.items():
        string += f'{k}: {v}\n'
    string = f'{{\n{string}}}'
    return string


def generate_diff(file1, file2):
    file1 = json.load(open(file1))
    file2 = json.load(open(file2))
    new_json = {}
    for key2, item2 in sorted(file2.items()):
        for key1, item1 in sorted(file1.items()):

            if key1 not in file2:
                new_key1 = ' - ' + key1
                new_json.update({new_key1: format_value(file1[key1])})

            else:
                if file1[key1] != file2[key1]:
                    new_key1 = ' - ' + key1
                    new_json.update({new_key1: format_value(file1[key1])})
                    new_key2 = ' + ' + key1
                    new_json.update({new_key2: format_value(file2[key1])})
                    break

                new_key1 = '   ' + key1
                new_json.update({new_key1: format_value(file1[key1])})

            if key2 not in file1:
                new_key2 = ' + ' + key2
                new_json.update({new_key2: format_value(file2[key2])})

    return to_string(new_json)
