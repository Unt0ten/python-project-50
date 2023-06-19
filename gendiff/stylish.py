from gendiff.internal_representation_tree import get_status, is_directory
from gendiff.internal_representation_tree import get_name, get_value
from gendiff.internal_representation_tree import get_children


NUM_INDENTS = 4
SHIFT_LEFT = 2
DIVE = 1


def get_nesting_depth(ident):
    return ident * NUM_INDENTS - SHIFT_LEFT


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


def make_new_node_name(name, status):
    if status == 'changed':
        new_name = '  ' + name
        return new_name
    elif status == 'deleted':
        new_name = '- ' + name
        return new_name
    elif status == 'added':
        new_name = '+ ' + name
        return new_name
    elif status == 'unchanged':
        new_name = '  ' + name
        return new_name


def stylish(tree):
    def format_stylish(tree, ident=1, symbol=" "):
        string = ''
        for node in tree:
            if is_directory(node):
                name = get_name(node)
                children = get_children(node)
                status = get_status(node)
                if status != 'unused':
                    new_name = make_new_node_name(name, status)
                    deep = get_nesting_depth(ident)
                    string += f'\n{symbol * deep}{new_name}: ' \
                              f'{{{format_stylish(children, ident + DIVE)}'
                else:
                    deep = get_nesting_depth(ident) + SHIFT_LEFT
                    string += f'\n{symbol * deep}{name}: ' \
                              f'{{{format_stylish(children, ident + DIVE)}'
                deep = get_nesting_depth(ident) + SHIFT_LEFT
                string += f'\n{symbol * deep}}}'
            else:
                name = get_name(node)
                value = get_value(node)
                status = get_status(node)
                if status != 'unused':
                    new_name = make_new_node_name(name, status)
                    deep = get_nesting_depth(ident)
                    string += f'\n{symbol * deep}{new_name}: ' \
                              f'{format_value(value)}'
                else:
                    deep = get_nesting_depth(ident) + SHIFT_LEFT
                    string += f'\n{symbol * deep}{name}: {format_value(value)}'

        return string

    result = format_stylish(tree)

    return f'{{{result}\n}}'
