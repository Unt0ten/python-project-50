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


def generate_diff(file_path1, file_path2):

    def inner(data1, data2):
        diff = {}
        for key in sorted(data1.keys() | data2.keys()):

            if key in data1 and key not in data2:
                new_key = '- ' + key
                diff.update({new_key: data1[key]})
            elif key not in data1 and key in data2:
                new_key = '+ ' + key
                diff.update({new_key: data2[key]})
            else:
                if data1[key] == data2[key]:
                    new_key = '  ' + key
                    diff.update({new_key: data1[key]})
                else:
                    if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                        new_key = '  ' + key
                        diff.update({new_key: inner(data1[key], data2[key])})
                    else:
                        new_key1 = '- ' + key
                        diff.update({new_key1: data1[key]})
                        new_key2 = '+ ' + key
                        diff.update({new_key2: data2[key]})

        return diff

    return inner(file_path1, file_path2)
