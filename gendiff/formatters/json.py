import json as json_dumps


def json(diff):
    '''Diff output in "json" format

    :param diff: formed diff in the form of a tree
    :return: string as "json" format

    '''
    return json_dumps.dumps(diff, indent=2)
