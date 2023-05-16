import base64

from util.error_handler import isBytes
from exceptions.exception import InvalidParamException


# Decodes from base64 to binary
def handle_decode(param):
    try:
        isBytes(param)
        return base64.b64decode(param)
    except (ValueError, TypeError, UnicodeDecodeError):
        raise InvalidParamException("Invalid param: {}".format(param))


# Encodes from binary to base64
def handle_encode(param):
    try:
        isBytes(param)
        return base64.b64encode(param)
    except (ValueError, TypeError, UnicodeDecodeError):
        raise InvalidParamException("Invalid param: {}".format(param))
