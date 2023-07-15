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

    return value


def get_nesting_depth(ident, status):
    '''Сalculating the length of indents of elements

    :param ident: nesting level
    :param status: node status
    :return: indent length

    '''
    if status is not None:
        return ident * NUM_INDENTS - SHIFT_LEFT
    return ident * NUM_INDENTS


def make_new_node_name(name, status):
    '''Generation of a new key name value depending on the status of the node

    :param name: node name
    :param status: node status
    :return: new name meaning

    '''
    if status == 'unchanged' or status == 'nested':
        name = '  ' + name

    elif status == 'deleted':
        name = '- ' + name

    elif status == 'added':
        name = '+ ' + name

    elif status == 'changed':
        new_name1 = '- ' + name
        new_name2 = '+ ' + name
        return new_name1, new_name2

    return name


def check_nesting(value, ident, symbol=' ', string=''):
    if isinstance(value, dict):
        for k, v in value.items():
            deep = NUM_INDENTS + ident + SHIFT_LEFT
            string += f'\n{symbol * deep}{k}: ' \
                      f'{check_nesting(format_value(v), ident + NUM_INDENTS)}'

        return f'{{{string}\n{symbol * (ident + SHIFT_LEFT)}}}'

    return value


def inner(diff, ident=DIVE):
    string = ''
    symbol = ' '

    for node in diff:
        name = node.get('name')
        value = format_value(node.get('value'))
        status = node.get('status')
        new_name = make_new_node_name(name, status)

        if status == 'nested':
            deep = get_nesting_depth(ident, status)
            string += f'\n{symbol * deep}{new_name}: ' \
                      f'{{{inner(check_nesting(value, deep), ident + DIVE)}'
            deep = NUM_INDENTS * ident
            string += f'\n{symbol * deep}}}'

        elif status == 'added' or status == 'deleted' or status == 'unchanged':
            deep = get_nesting_depth(ident, status)
            string += f'\n{symbol * deep}{new_name}: ' \
                      f'{check_nesting(value, deep)}'

        elif status == 'changed':
            del_name, add_name = make_new_node_name(name, status)
            old_value = format_value(node.get('old_value'))
            new_value = format_value(node.get('new_value'))
            deep = get_nesting_depth(ident, status)
            string += f'\n{symbol * deep}{del_name}: ' \
                      f'{check_nesting(old_value, deep)}'
            string += f'\n{symbol * deep}{add_name}: ' \
                      f'{check_nesting(new_value, deep)}'

    return string


def stylish(diff):
    '''Diff output in "stylish" format

    :param diff: formed diff in the form of a tree
    :return: string as "stylish" format

    '''

    formatted_output = inner(diff)

    return f'{{{formatted_output}\n}}'
