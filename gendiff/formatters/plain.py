def format_value(value):
    '''
    Final value conversion

    :param value: node value
    :return: final result

    '''
    if isinstance(value, list) or isinstance(value, dict):
        value = "[complex value]"

    elif value is None:
        value = 'null'

    elif isinstance(value, bool):
        value = str(value).lower()

    elif not isinstance(value, int):
        value = f"'{value}'"

    return value


def inner(diff, path):
    formatted_output = ''

    for node in diff:

        value = node.get('value', '')
        status = node['status']
        path_copy = path.copy()
        path_copy.append(node['name'])

        if status == 'nested':
            formatted_output += f'{inner(value, path_copy)}\n'

        elif status == 'changed':
            old = format_value(node.get('old_value', ''))
            new = format_value(node.get('new_value', ''))
            formatted_output += f"Property '{'.'.join(path_copy)}' " \
                                f"was updated. From {old} to {new}\n"

        elif status == 'added':
            formatted_output += f"Property '{'.'.join(path_copy)}' " \
                                f"was added with value: " \
                                f"{format_value(value)}\n"

        elif status == 'deleted':
            formatted_output += f"Property '{'.'.join(path_copy)}' " \
                                f"was removed\n"

    return formatted_output.strip()


def plain(diff):
    '''Diff output in "plain" format

    :param diff: formed diff in the form of a tree
    :return: string as "plain" format

    '''
    return inner(diff, [])
