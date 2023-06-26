def format_value(value):
    '''
    This function formats bool and Nonetype dictionary values from .py to .json.
    '''
    if value is None:
        return 'null'

    elif isinstance(value, bool):
        return str(value).lower()

    else:
        return value
