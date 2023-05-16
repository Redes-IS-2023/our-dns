import socket

bin_file = "sample/out/package.bin"

# Inits a DNS/UDP socket:53
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 53))

# Listen for incoming DNS requests
while True:
    data, addr = sock.recvfrom(1024)
    # dns_query = data[12:]  # Skip the DNS header
    # ip_addr = addr[0]

    # Write the DNS query to a file
    with open(bin_file, "wb") as f:
        f.write(data)
