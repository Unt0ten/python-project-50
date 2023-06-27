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
    '''Сalculating the length of indents of elements

    :param ident: nesting level
    :param status: node status
    :return: indent length

    '''
    if status != 'unused':
        return ident * NUM_INDENTS - SHIFT_LEFT
    return ident * NUM_INDENTS


def make_new_node_name(name, status):
    '''Generation of a new key name value depending on the status of the node

    :param name: node name
    :param status: node status
    :return: new name meaning

    '''
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
    '''Formation of the internal representation
        of the node not included in the diff

    :param value: node value
    :return: new node

    '''
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


def stylish(diff):
    '''Diff output in "stylish" format

    :param diff: formed diff in the form of a tree
    :return: string as "plain" format

    '''
    def inner(diff, ident=DIVE, symbol=' '):
        string = ''

        for node in diff:

            name = get_name(node)
            value = make_inner(get_value(node))
            status = get_status(node)
            new_name = make_new_node_name(name, status)

            if isinstance(value, list):
                deep = get_nesting_depth(ident, status)
                string += f'\n{symbol * deep}{new_name}: ' \
                          f'{{' \
                          f'{inner(format_value(value), ident + DIVE)}'

                deep = NUM_INDENTS * ident
                string += f'\n{symbol * deep}}}'

            else:
                deep = get_nesting_depth(ident, status)
                string += f'\n{symbol * deep}{new_name}: {format_value(value)}'

        return string

    result = inner(diff)

    return f'{{{result}\n}}'
