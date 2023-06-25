from gendiff.formatters.format_value_module import format_value
from gendiff.internal_representation_tree import get_value, get_name, get_status


def check_complex(value):
    if isinstance(value, list) or isinstance(value, dict):
        return "[complex value]"
    return value


def get_value_updated(node, status):
    if status == 'upd_add':
        return format_value(get_value(node))
    elif status == 'upd_del':
        return format_value(get_value(node))


def set_quotes(value):
    results = ['true', 'false', 'null', '[complex value]']

    if value in results or isinstance(value, int):
        return value

    return f"'{value}'"


def convert_value(value):
    result = set_quotes(format_value(check_complex(value)))
    return result


def make_string_flat(path, value, status):
    string = ''

    if status == 'added':
        string += f"Property '{'.'.join(path)}' " \
                  f"was added with value: {convert_value(value)}\n"

    elif status == 'deleted':
        string += f"Property '{'.'.join(path)}' was removed\n"

    return string


def make_string_nested(path, node, status):
    string = ''

    if status == 'upd_del':
        old = convert_value(get_value_updated(node, 'upd_del'))
        string += f"Property '{'.'.join(path)}' was updated. From {old}"

    elif status == 'upd_add':
        new = convert_value(get_value_updated(node, 'upd_add'))
        string += f" to {new}\n"

    return string


def plain(tree):
    def inner(tree, path):

        string = ''

        for node in tree:

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

    result = inner(tree, []).strip()

    return result
