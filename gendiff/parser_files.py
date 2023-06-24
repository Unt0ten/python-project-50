import yaml
from yaml.loader import SafeLoader
import json


def get_data(file):
    '''Parsing json and yaml files'''

    if file.endswith('.json'):
        result = json.load(open(file))

    elif file.endswith('.yml') or file.endswith('.yaml'):
        result = yaml.load(open(file), Loader=SafeLoader)

    return result
