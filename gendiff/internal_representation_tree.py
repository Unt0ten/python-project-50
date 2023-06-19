def isdict(data):
    return isinstance(data, dict)


def make_node(key, value, status='unused'):
    """Return node"""
    if isinstance(value, list):
        for elem in value:
            if isdict(elem):
                return {
                    'name': key,
                    'children': value,
                    'status': status,
                    'type': 'directory',
                    }
    return {
        'name': key,
        'value': value,
        'status': status,
        'type': 'leaf',
        }


def is_directory(node):
    """Check is node a directory"""
    return node['type'] == 'directory'


def get_children(directory):
    """Return children of directory"""
    return directory['children']


def get_value(leaf):
    """Return value of leaf"""
    return leaf['value']


def get_status(node):
    """Return status of node"""
    return node['status']


def get_name(node):
    """Return name of node"""
    return node['name']


def determine_status_node(node):
    if get_name(node).startswith('  '):
        node['status'] = 'changed'
        node['name'] = get_name(node).replace('  ', '')
    elif get_name(node).startswith('- '):
        node['status'] = 'deleted'
        node['name'] = get_name(node).replace('- ', '')
    elif get_name(node).startswith('+ '):
        node['status'] = 'added'
        node['name'] = get_name(node).replace('+ ', '')
    elif get_name(node).startswith('=='):
        node['status'] = 'unchanged'
        node['name'] = get_name(node).replace('==', '')


def get_diff_data(data1, data2):
    diff = {}
    for key in sorted(data1.keys() | data2.keys()):

        if key in data1 and key not in data2:
            new_key = '- ' + key
            diff.update({new_key: data1[key]})
        elif key not in data1 and key in data2:
            new_key = '+ ' + key
            diff.update({new_key: data2[key]})
        else:
            if data1[key] == data2[key]:
                new_key = '==' + key
                diff.update({new_key: data1[key]})
            else:
                if isdict(data1[key]) and isdict(data2[key]):
                    new_key = '  ' + key
                    diff.update(
                        {new_key: get_diff_data(data1[key], data2[key])})
                else:
                    new_key1 = '- ' + key
                    diff.update({new_key1: data1[key]})
                    new_key2 = '+ ' + key
                    diff.update({new_key2: data2[key]})

    return diff


def gen_tree(data):
    tree = []
    for key in data.keys():
        if isdict(data[key]):
            node = make_node(key, gen_tree(data[key]))
            determine_status_node(node)
            tree.append(node)
        else:
            node = make_node(key, data[key])
            determine_status_node(node)
            tree.append(node)
    return tree
