# from gendiff.parser_files import load_content
# from gendiff.parser_files import parse_content
# 
# 
# def read(file_path):
#     with open(file_path, 'r') as f:
#         result = f.read()
#     return result
# 
# 
# def test_load_content_json():
#     file_path = 'tests/fixtures/file1.json'
#     result = {"host": "hexlet.io", "timeout": 50,
#               "proxy": "123.234.53.22",
#               "follow": False}
# 
#     assert load_content(file_path) == result
# 
# 
# def test_load_content_yaml():
#     file_path = 'tests/fixtures/file1.yaml'
#     result = {'author': 'Charles R. Saunders', 'language': 'English',
#               'publication-year': 1981,
#               'pages': 224}
# 
#     assert load_content(file_path) == result
# 
# 
# def test_load_content_yml():
#     file_path = 'tests/fixtures/file.yml'
#     result = {'author': 'Charles R. Saunders', 'language': 'English',
#               'publication-year': 1981,
#               'pages': 224}
# 
#     assert load_content(file_path) == result
# 
# 
# def test_parse_content_json():
#     data = read('tests/fixtures/file1.json')
#     extension = '.json'
#     result = {"host": "hexlet.io", "timeout": 50,
#               "proxy": "123.234.53.22",
#               "follow": False}
#     
#     assert parse_content(data, extension) == result
# 
# 
# def test_parse_content_yaml():
#     data = read('tests/fixtures/file1.yaml')
#     extension = '.yaml'
#     result = {'author': 'Charles R. Saunders', 'language': 'English',
#               'publication-year': 1981,
#               'pages': 224}
#     
#     assert parse_content(data, extension) == result