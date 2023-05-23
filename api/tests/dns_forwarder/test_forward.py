import pytest
from api.dns_forwarder import forward
from api.exceptions.exception import UnreachableHostException


def test_forward_success():
    domain_mock = "com/google"
    response = forward(domain_mock)
    assert type(response) == dict

def test_forward_fails():
    domain_mock = "this/host/does/not/exist"
    with pytest.raises(UnreachableHostException):
        forward(domain_mock)
