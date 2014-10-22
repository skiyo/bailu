"""
Recursively convert unicode to str using utf-8
"""
def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, tuple):
        return tuple([convert(element) for element in input])
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

