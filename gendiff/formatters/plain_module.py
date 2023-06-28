from gendiff.formatters.format_value_module import format_value
from gendiff.internal_representation_diff import get_value, get_name, get_status


def check_complex(value):
    '''Checking the node value for complexity'''
    if isinstance(value, list) or isinstance(value, dict):
        return "[complex value]"
    return value


def get_value_updated(node, status):
    '''
    Node value conversion

    :param node: formed diff node
    :param status: status of the generated diff node
    :return: final result

    '''
    if status == 'upd_add':
        return format_value(get_value(node))
    elif status == 'upd_del':
        return format_value(get_value(node))


def set_quotes(value):
    '''Wrapping the value in quotes for output'''
    results = ['true', 'false', 'null', '[complex value]']

    if value in results or isinstance(value, int):
        return value

    return f"'{value}'"


def convert_value(value):
    '''
    Final value conversion

    :param value: node value
    :return: final result

    '''
    result = set_quotes(format_value(check_complex(value)))
    return result


def make_string_flat(path, value, status):
    '''
    Formation of a line depending on the status

    :param path: path to the root of the modified value
    :param value: node value
    :param status: status of the generated diff node
    :return: a formed string

    '''
    string = ''

    if status == 'added':
        string += f"Property '{'.'.join(path)}' " \
                  f"was added with value: {convert_value(value)}\n"

    elif status == 'deleted':
        string += f"Property '{'.'.join(path)}' was removed\n"

    return string


def make_string_nested(path, node, status):
    '''
    Formation of a line depending on the status

    :param path: path to the root of the modified value
    :param node: formed diff node
    :param status: status of the generated diff node
    :return: a formed string

    '''
    string = ''

    if status == 'upd_del':
        old = convert_value(get_value_updated(node, 'upd_del'))
        string += f"Property '{'.'.join(path)}' was updated. From {old}"

    elif status == 'upd_add':
        new = convert_value(get_value_updated(node, 'upd_add'))
        string += f" to {new}\n"

    return string


def plain(diff):
    '''Diff output in "plain" format

    :param diff: formed diff in the form of a tree
    :return: string as "plain" format

    '''
    def inner(diff, path):
        '''

        :param path: path to the root of the modified value
        :return: string

        '''
        string = ''

        for node in diff:

            name = get_name(node)
            value = format_value(get_value(node))
            status = get_status(node)
            path_copy = path.copy()
            path_copy.append(name)

            if status == 'changed':
                string += inner(value, path_copy)

            string += make_string_flat(path_copy, value, status)
            string += make_string_nested(path_copy, node, status)

        return string

    result = inner(diff, []).strip()

    return result
