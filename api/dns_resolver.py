import struct
import socket
from firebase_admin import db


# Search for a DNS entry on the firebase db
# @param dns_message: DNSRecord
# @returns firebase response if found
def resolve(dns_message):
    domain_name = dns_message.q.qname.__str__()
    domain_path = "/".join(domain_name.split(".")[::-1])
    return db.reference(domain_path).get()


# Builds an dns package
# @param query_id: int
# @param query_domain: string
# @param resolved_ip: string
# @returns bytes
# @source: https://datatracker.ietf.org/doc/html/rfc1035#section-4.1.1
def build_dns_response(query_id, query_domain, resolved_ip):
    flag = 0x8180  # Standard DNS response flag for no error
    q_count = 1  # Number of questions
    a_count = 1  # Number of answers
    auth_count = 0  # Number of authoritative records
    other_count = 0  # Number of additional records

    # Build DNS response packet
    dns_packet = struct.pack(
        "!HHHHHH", query_id, flag, q_count, a_count, auth_count, other_count
    )

    # Add the query domain to the response packet
    for part in query_domain.split("."):
        dns_packet += struct.pack("!B", len(part)) + part.encode("utf-8")
    dns_packet += struct.pack("!B", 0)  # Null-terminator for the domain name

    # Add query type A record and class IN
    dns_packet += struct.pack("!HH", 0x0001, 0x0001)

    # Add the answer resource record A record
    dns_packet += struct.pack("!HHHLH", 0xC00C, 0x0001, 0x0001, 300, 4)

    # Add the resolved IP
    dns_packet += socket.inet_aton(resolved_ip)

    return dns_packet
