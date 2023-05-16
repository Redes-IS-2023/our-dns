from firebase_admin import db


# Search for a DNS entry on the firebase db
# @param dns_message: DNSRecord
# @returns firebase response if found
def resolve(dns_message):
    domain_name = dns_message.q.qname.__str__()
    domain_path = "/".join(domain_name.split(".")[::-1])
    return db.reference(domain_path).get()
