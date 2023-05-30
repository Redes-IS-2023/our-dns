import configparser
import os
from firebase_admin import credentials, firestore, initialize_app

base_dir = os.path.dirname(os.path.abspath(__file__))

config = configparser.ConfigParser()
config_path = os.path.join(base_dir, "config.ini")
config.read(config_path)
cred_fname = config.get("DEFAULT", "cred_fname")
cred_path = os.path.join(base_dir, "cred", cred_fname)

def get_code_from_ip(ip_address):
    # Initialize Firebase Admin SDK
    cred = credentials.Certificate(cred_path)
    initialize_app(cred)

    # Creates a firestore client
    db = firestore.client()

    # Query Firestore to retrieve the code based on the 'from' range
    query_from = db.collection('your_collection_name') \
        .where('from', '<=', ip_address) \
        .order_by('from', direction=firestore.Query.DESCENDING) \
        .limit(1)
    docs_from = query_from.get()

    # Query Firestore to retrieve the code based on the 'to' range
    query_to = db.collection('your_collection_name') \
        .where('to', '>=', ip_address) \
        .order_by('to', direction=firestore.Query.ASCENDING) \
        .limit(1)
    docs_to = query_to.get()

    # Merge the results and retrieve the code
    merged_docs = docs_from + docs_to
    for doc in merged_docs:
        data = doc.to_dict()
        code = data.get('code')
        if code:
            return code
    return None

# Example usage
ip_address = '192.168.1.10'
code = get_code_from_ip(ip_address)
if code:
    print(f"Code for IP address {ip_address}: {code}")
else:
    print(f"No matching code found for IP address {ip_address}")
