import configparser
import os
import gzip
import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

base_dir = os.path.dirname(os.path.abspath(__file__))

config = configparser.ConfigParser()
config_path = os.path.join(base_dir, "../api/config.ini")
config.read(config_path)
cred_fname = config.get("DEFAULT", "cred_fname")

# Initialize Firebase Admin SDK
cred_path = os.path.join(base_dir, "../api/cred", cred_fname)
print(cred_path)
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# Creates a firestore client
db = firestore.client()

# Uploads data to firestore
def upload_data(collection_name, data_list):
    for data in data_list:
        doc_ref = db.collection(collection_name).document()
        doc_ref.set(data)
    print("Data uploaded successfully.")


# Uncompresses data and reads the csv file
def uncompress_and_read_csv(file_path):
    try:
        # Uncompress the .gz file
        with gzip.open(file_path, 'rt') as gz_file:
            # Read the uncompressed file as CSV
            csv_reader = csv.reader(gz_file)
            
            # Iterate over each row in the CSV file
            result = []
            for row in csv_reader:
                # Formats data
                data = {
                    'from': row[0],
                    'to': row[1],
                    'code': row[2]
                }
                result.append(data)
                
        print("CSV file read successfully.")
        return result
    
    except FileNotFoundError:
        print("File not found.")
    
    except gzip.BadGzipFile:
        print("Invalid .gz file.")

# Uncompress and processes file
db_path = os.path.join(base_dir, "dbip-country-lite-2023-05.csv.gz")
data = uncompress_and_read_csv(db_path)

# Upload data to Firestore
upload_data('geo', data)
