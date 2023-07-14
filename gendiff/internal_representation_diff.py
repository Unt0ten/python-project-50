def isdict(data):
    '''Whether the object is a dictionary'''
    return isinstance(data, dict)


def make_node(key, value, status):
    """Return node"""
    return {
        'name': key,
        'value': value,
        'status': status}


def get_diff_data(data1, data2):
    '''Returns the difference as a dictionary with information about changes
    to keys and their values'''
    diff = []
    deleted_keys = data1.keys() - data2.keys()
    added_keys = data2.keys() - data1.keys()

    for key in sorted(data1.keys() | data2.keys()):

        if key in deleted_keys:
            node = make_node(key, data1[key], 'deleted')
            diff.append(node)

        elif key in added_keys:
            node = make_node(key, data2[key], 'added')
            diff.append(node)

        elif data1[key] == data2[key]:
            node = make_node(key, data1[key], 'unchanged')
            diff.append(node)

        elif isdict(data1[key]) and isdict(data2[key]):
            node = make_node(key, get_diff_data(data1[key], data2[key]),
                             'nested')
            diff.append(node)

        else:
            node = {'name': key,
                    'old_value': data1[key],
                    'new_value': data2[key],
                    'status': 'changed'}
            diff.append(node)

    return diff
