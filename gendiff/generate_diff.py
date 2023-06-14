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
    '''
    The diff is built based on how the content in the second file has changed
    relative to the first.
    Keys are displayed in alphabetical order.

    The absence of a plus or minus indicates that the key is in both files,
    and its values are the same.
    In all other situations, the key value is either different,
    or the key is in only one file.
    '''
    new_dict = {}
    for key2, item2 in sorted(file2.items()):
        for key1, item1 in sorted(file1.items()):

            if key1 not in file2:
                new_key1 = ' - ' + key1
                new_dict.update({new_key1: format_value(file1[key1])})

            else:
                if file1[key1] != file2[key1]:
                    new_key1 = ' - ' + key1
                    new_dict.update({new_key1: format_value(file1[key1])})
                    new_key2 = ' + ' + key1
                    new_dict.update({new_key2: format_value(file2[key1])})

                else:
                    new_key1 = '   ' + key1
                    new_dict.update({new_key1: format_value(file1[key1])})

            if key2 not in file1:
                new_key2 = ' + ' + key2
                new_dict.update({new_key2: format_value(file2[key2])})

    return to_string(new_dict)
