from gendiff.internal_representation_tree import get_diff_data
from gendiff.parser_files import get_data
from gendiff.formatters.stylish_module import stylish
from gendiff.formatters.plain_module import plain
from gendiff.formatters.json_module import make_json as json


def generate_diff(file_path1, file_path2, formatter=stylish):
    data1, data2 = get_data(file_path1), get_data(file_path2)
    diff = get_diff_data(data1, data2)
    result = formatter(diff)
    return result
