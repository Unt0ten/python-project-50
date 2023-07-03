from gendiff.internal_representation_diff import get_diff_data
from gendiff.parser_files import load_content
from gendiff.formater import apply_format


def generate_diff(file_path1, file_path2, formater='stylish'):
    '''Diff generator and its output in the selected formatter
    (default 'stylish')

    :param file_path1: path to first file
    :param file_path2: path to second file
    :param formater: formater selection "stylish"/"plain"/"json"
    :return: final diff output

    '''
    data1, data2 = load_content(file_path1), load_content(file_path2)
    diff = get_diff_data(data1, data2)
    result = apply_format(diff, formater)
    return result
