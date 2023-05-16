import base64
import dns.query
import dns.message

package_file = "sample/package.bin"
b64_file = "sample/b64.txt"


# Test if the package.bin resolves correctly in the 8.8.8.8 server
def test_package_bin():
    # Read the binary data from the file
    with open(package_file, "rb") as f:
        binary_data = f.read()

    # Create a DNS message object from the binary data
    dns_query = dns.message.from_wire(binary_data)

    # Send the query using UDP to 8.8.8.8 DNS server
    return dns.query.udp(dns_query, "8.8.8.8")


def test_b64():
    # Read the binary data from the file
    with open(b64_file, "rb") as f:
        encoded_data = f.read()
    decoded_data = base64.b64decode(encoded_data)

    # Create a DNS message object from the binary data
    dns_query = dns.message.from_wire(decoded_data)

    # Send the query using UDP to 8.8.8.8 DNS server
    return dns.query.udp(dns_query, "8.8.8.8")


response = test_package_bin()
print("test_package_bin\n", response)

response = test_b64()
print("\ntest_b64\n", response)
