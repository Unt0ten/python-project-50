from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json


def apply_format(diff, formatter):
    '''Choice of formatters (default "stylish")'''
    if formatter == 'stylish':
        return stylish(diff)

    elif formatter == 'plain':
        return plain(diff)

    elif formatter == 'json':
        return json(diff)
