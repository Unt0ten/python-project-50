import yaml
from yaml.loader import SafeLoader
import json
import os


def load_content(file_path):
    _, extension = os.path.splitext(file_path)
    with open(file_path, 'r') as file:
        data = file.read()

    return parse_content(data, extension)


def parse_content(data, extension):
    if extension == '.json':
        return json.loads(data)

    elif extension == '.yml' or extension == '.yaml':
        return yaml.load(data, Loader=SafeLoader)
