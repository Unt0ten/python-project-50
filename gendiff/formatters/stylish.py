from gendiff.internal_representation_diff import make_node

NUM_INDENTS = 4
SHIFT_LEFT = 2
DIVE = 1


def format_value(value):
    '''This function formats bool and Nonetype
        dictionary values from .py to .json.'''
    if value is None:
        return 'null'

    elif isinstance(value, bool):
        return str(value).lower()

    else:
        return value


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
    if status == 'unchanged' or status == 'nested':
        new_name = '  ' + name
        return new_name

    elif status == 'deleted':
        new_name = '- ' + name
        return new_name

    elif status == 'added':
        new_name = '+ ' + name
        return new_name

    elif status == 'changed':
        new_name1 = '- ' + name
        new_name2 = '+ ' + name
        return new_name1, new_name2

    return name


def make_inner(value):
    '''Formation of the internal representation
        of the node not included in the diff

    :param value: node value
    :return: new node

    '''
    new_node = []

    if isinstance(value, dict):
        for key in value.keys():

            if isinstance(value[key], dict):
                node = [make_node(key, make_inner(value[key]))]
                new_node.extend(node)

            else:
                node = [make_node(key, value[key])]
                new_node.extend(node)
    else:
        new_node = value

    return new_node


def make_string(new_name, status, value, func, ident):
    symbol = ' '
    string = ''
    if isinstance(value, list):
        deep = get_nesting_depth(ident, status)
        string += f'\n{symbol * deep}{new_name}: ' \
                  f'{{{func(format_value(value), ident + DIVE)}'

        deep = NUM_INDENTS * ident
        string += f'\n{symbol * deep}}}'

    else:
        deep = get_nesting_depth(ident, status)
        string += f'\n{symbol * deep}{new_name}: {format_value(value)}'

    return string


def stylish(diff):
    '''Diff output in "stylish" format

    :param diff: formed diff in the form of a tree
    :return: string as "plain" format

    '''

    def inner(diff, ident=DIVE):
        string = ''

        for node in diff:
            name = node['name']
            value = make_inner(node.get('value', ''))
            old_value = make_inner(node.get('old_value', ''))
            new_value = make_inner(node.get('new_value', ''))
            status = node['status']
            new_name = make_new_node_name(name, status)

            if status != 'changed':
                string += make_string(new_name, status, value, inner, ident)

            else:
                del_name, add_name = make_new_node_name(name, status)
                string += make_string(del_name, status, old_value, inner, ident)
                string += make_string(add_name, status, new_value, inner, ident)

        return string

    formatted_output = inner(diff)

    return f'{{{formatted_output}\n}}'
