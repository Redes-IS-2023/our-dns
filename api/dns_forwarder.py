import ast
import configparser
import os
import dns.resolver
import dns.query
import dns.message
from util.error_handler import isBytes


from exceptions.exception import UnreachableHostException


# Get current project path
base_dir = os.path.dirname(os.path.abspath(__file__))

# Access the config file properties
config = configparser.ConfigParser()
config_path = os.path.join(base_dir, "config.ini")
config.read(config_path)
forwarder_servers = ast.literal_eval(config.get("DNS.RESOLVER", "forwarder_servers"))

# Create a DNS resolver object
resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = forwarder_servers


# Tries to forward host resolution to alternative DNS servers
def forward(domain):
    try:
        domain = domain.split("/")
        domain = ".".join(reversed(domain))
        response = resolver.resolve(domain, "A")
        return {domain: response[0].address}
    except:
        raise UnreachableHostException("Domain not found: {}".format(domain))


# Tries to forward host resolution to alternative DNS servers
# @param dns_package_b: bytes
# @return bytes
def forward_package(dns_package_b):
    try:
        isBytes(dns_package_b)
        dns_query = dns.message.from_wire(dns_package_b)
        return dns.query.udp(dns_query, "8.8.8.8").to_wire()
    except:
        raise UnreachableHostException("Domain not found: {}".format(dns_query))
