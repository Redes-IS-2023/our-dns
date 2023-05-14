import base64

from exceptions.exception import InvalidParamException


# Decodes from base64 to UTF-8
def handle_decode(param):
    try:
        return base64.b64decode(param).decode("utf-8")
    except (ValueError, TypeError, UnicodeDecodeError):
        raise InvalidParamException("Invalid param: {}".format(param))
