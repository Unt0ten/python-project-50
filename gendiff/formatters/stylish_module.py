from gendiff.internal_representation_tree import get_status
from gendiff.internal_representation_tree import get_name
from gendiff.internal_representation_tree import get_value
from gendiff.internal_representation_tree import isdict
from gendiff.internal_representation_tree import make_node
from gendiff.formatters.format_value_module import format_value

NUM_INDENTS = 4
SHIFT_LEFT = 2
DIVE = 1


def get_nesting_depth(ident, status):
    if status != 'unused':
        return ident * NUM_INDENTS - SHIFT_LEFT
    return ident * NUM_INDENTS


def make_new_node_name(name, status):
    if status == 'changed' or status == 'unchanged':
        new_name = '  ' + name
        return new_name

    elif status == 'deleted' or status == 'upd_del':
        new_name = '- ' + name
        return new_name

    elif status == 'added' or status == 'upd_add':
        new_name = '+ ' + name
        return new_name

    elif status == 'unused':
        return name


def make_inner(value):
    new_node = []

    if isdict(value):
        for key in value.keys():

            if isdict(value[key]):
                node = [make_node(key, make_inner(value[key]))]
                new_node.extend(node)

            else:
                node = [make_node(key, value[key])]
                new_node.extend(node)
    else:
        new_node = value

    return new_node


def stylish(tree):
    def format_stylish(tree, ident=DIVE, symbol=' '):

        string = ''

        for node in tree:

            name = get_name(node)
            value = make_inner(get_value(node))
            status = get_status(node)
            new_name = make_new_node_name(name, status)

            if isinstance(value, list):
                deep = get_nesting_depth(ident, status)
                string += f'\n{symbol * deep}{new_name}: ' \
                          f'{{{format_stylish(format_value(value), ident + DIVE)}'

                deep = NUM_INDENTS * ident
                string += f'\n{symbol * deep}}}'

            else:
                deep = get_nesting_depth(ident, status)
                string += f'\n{symbol * deep}{new_name}: {format_value(value)}'

        return string

    result = format_stylish(tree)

    return f'{{{result}\n}}'
