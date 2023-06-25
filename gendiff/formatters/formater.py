from gendiff.formatters.stylish_module import stylish
from gendiff.formatters.plain_module import plain
from gendiff.formatters.json_module import make_json


def apply_format(diff, formater):
    if formater == 'stylish':
        return stylish(diff)

    elif formater == 'plain':
        return plain(diff)

    elif formater == 'json':
        return make_json(diff)
