import os
import configparser
import firebase_admin

from firebase_admin import credentials, db
from flasgger import Swagger, swag_from
from flask import Flask, jsonify, request
from dns_resolver import build_dns_response, resolve
from dns_forwarder import forward, forward_package
from dnslib import DNSRecord
from exceptions.exception import InvalidParamException, UnreachableHostException
from util.b64coder import handle_decode, handle_encode
from swagger_doc.doc import *

# Get current project path
base_dir = os.path.dirname(os.path.abspath(__file__))

# Access the config file properties
config = configparser.ConfigParser()
config_path = os.path.join(base_dir, "config.ini")
config.read(config_path)
cred_fname = config.get("DEFAULT", "cred_fname")
firebase_url = config.get("DEFAULT", "firebase_url")

# Initialize Firebase credentials
cred_path = os.path.join(base_dir, "cred", cred_fname)
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {"databaseURL": firebase_url})

# Initialize Flask & Swagger app
app = Flask(__name__)
swagger = Swagger(app)


# Define endpoint to redirect encoded package to DNS server
@app.route("/api/dns_resolver/", methods=["POST"])
@swag_from(post_dns_package_ep_doc)
def post_dns_package():
    decoded_package = handle_decode(request.data)
    dns_message = DNSRecord.parse(decoded_package)
    response = resolve(dns_message)

    # Forwarding to external DNS server
    if response is None:
        response = forward_package(decoded_package)
        encoded_reply = handle_encode(response)
    else:  # Resolve using Firebase db
        domain = str(dns_message.q.qname)
        package = build_dns_response(dns_message.header.id, domain, response["resolve"])
        encoded_reply = handle_encode(package)

    return encoded_reply


# Define testing endpoint to retrieve data from Firebase
@app.route("/api/dns/testing/<param>", methods=["GET"])
@swag_from(get_dns_testing_ep_doc)
def get_dns_testing(param):
    param = "/".join(param.split(".")[::-1])
    ref = db.reference(param)
    response = ref.get()

    # Forwarding to external DNS server
    if response is None:
        response = forward(param)

    return jsonify(response)


# Define endpoint to retrieve all records data from Firebase
@app.route("/api/records/", methods=["GET"])
@swag_from(get_dns_records_ep_doc)
def get_dns_records():
    ref = db.reference("/")
    response = ref.get()
    return jsonify(response)


# Define endpoint to retrieve one record data from Firebase
@app.route("/api/record/<param>", methods=["GET"])
@swag_from(get_dns_record_ep_doc)
def get_dns_record(param):
    param = "/".join(param.split(".")[::-1])
    ref = db.reference(param)
    response = ref.get()
    return jsonify(response)


@app.errorhandler(InvalidParamException)
def handle_invalid_param(error):
    response = jsonify({"code": 400, "error": str(error)})
    response.status_code = 400
    return response


@app.errorhandler(UnreachableHostException)
def handle_unreachable_host(error):
    response = jsonify({"code": 404, "error": str(error)})
    response.status_code = 404
    return response


# Run the app on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0")
