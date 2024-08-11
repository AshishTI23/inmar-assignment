import ast
import json


def boolean_eval(value):
    """Returns boolean interpretation of the given value."""
    if isinstance(value, (str, bytes)):
        try:
            value = json.loads(value)
        except ValueError:
            try:
                value = ast.literal_eval(value)
            except (ValueError, SyntaxError):
                pass
            else:
                return boolean_eval(value=value)
        else:
            return boolean_eval(value=value)

    return bool(value)
