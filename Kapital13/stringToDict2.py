import ast

def convert_string_to_dict(string):
    # Remove leading and trailing whitespace, if any
    string = string.strip()

    # Use the ast module to safely evaluate the string as a literal
    try:
        dictionary = ast.literal_eval(string)
        if not isinstance(dictionary, dict):
            raise ValueError('Input is not a valid dictionary')
    except (ValueError, SyntaxError) as e:
        raise ValueError('Input is not a valid dictionary') from e

    return dictionary

string = '{"1. Key": 34, "2. Key": 446, "3. Key": 4}'
dictionary = convert_string_to_dict(string)
print(dictionary)
