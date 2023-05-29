from api.dns_resolver import build_dns_response

def test_build_dns_response():
    id = 1
    domain = 'google.com'
    ip = '8.8.8.8'
    expected = b'\x00\x01\x81\x80\x00\x01\x00\x01\x00\x00\x00\x00\x06google\x03com\x00\x00\x01\x00\x01\xc0\x0c\x00\x01\x00\x01\x00\x00\x01,\x00\x04\x08\x08\x08\x08'
    dns_response = build_dns_response(id, domain, ip)
    assert dns_response == expected
