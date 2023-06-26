from gendiff.internal_representation_tree import get_diff_data
from gendiff.parser_files import get_data
from gendiff.formatters.formater import apply_format


def generate_diff(file_path1, file_path2, formater='stylish'):
    '''Diff generator and its output in the selected formatter
    (default 'stylish')

    :param file_path1: path to first file
    :param file_path2: path to second file
    :param formater: formatter selection "stylish"/"plain"/"json"
    :param return: final diff output

    '''
    data1, data2 = get_data(file_path1), get_data(file_path2)
    diff = get_diff_data(data1, data2)
    result = apply_format(diff, formater)
    return result
