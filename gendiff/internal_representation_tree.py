def isdict(data):
    return isinstance(data, dict)


def make_node(key, value, status='unused'):
    """Return node"""

    return {
        'name': key,
        'value': value,
        'status': status,
        }


def get_value(node):
    return node['value']


def get_status(node):
    """Return status of node."""
    return node.get('status', '')


def get_name(node):
    """Return name of node."""
    return node['name']


def get_diff_data(data1, data2):
    '''
    Returns the difference as a dictionary with information about changes
    to keys and their values
    '''

    diff = []
    for key in sorted(data1.keys() | data2.keys()):

        if key in data1 and key not in data2:
            node = make_node(key, data1[key], 'deleted')
            diff.append(node)

        elif key not in data1 and key in data2:
            node = make_node(key, data2[key], 'added')
            diff.append(node)

        else:
            if data1[key] == data2[key]:
                node = make_node(key, data1[key], 'unchanged')
                diff.append(node)

            else:
                if isdict(data1[key]) and isdict(data2[key]):
                    node = make_node(key, get_diff_data(data1[key], data2[key]),
                                     'changed')
                    diff.append(node)

                else:
                    node = make_node(key, data1[key], 'upd_del')
                    diff.append(node)
                    node = make_node(key, data2[key], 'upd_add')
                    diff.append(node)

    return diff
