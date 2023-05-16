from exceptions.exception import InvalidParamException


def isBytes(param):
    if type(param) != bytes:
        raise InvalidParamException("Expected bytes, but received: {}".format(param))
