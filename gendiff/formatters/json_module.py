import json


def make_json(diff):
    '''Diff output in "json" format

    :param diff: formed diff in the form of a tree
    :return: string as "json" format

    '''
    return json.dumps(diff, indent=2)
