from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json


def apply_format(diff, formater):
    '''Choice of formatters (default "stylish")'''
    if formater == 'stylish':
        return stylish(diff)

    elif formater == 'plain':
        return plain(diff)

    elif formater == 'json':
        return json(diff)
