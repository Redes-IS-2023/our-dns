import json
import os
import configparser
import firebase_admin
import requests

from firebase_admin import credentials, db, firestore
from flasgger import Swagger, swag_from
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from dnslib import DNSRecord

from api.dns_forwarder import forward, forward_package
from api.dns_resolver import build_dns_response, resolve
from api.exceptions.exception import InvalidParamException, UnreachableHostException
from api.swagger_doc.doc import *
from api.util.b64coder import handle_decode, handle_encode

# Get current project path
base_dir = os.path.dirname(os.path.abspath(__file__))

# Access the config file properties
config = configparser.ConfigParser()
config_path = os.path.join(base_dir, "config.ini")
config.read(config_path)
cred_fname = config.get("DEFAULT", "cred_fname")
firebase_url = config.get("DEFAULT", "firebase_url")
collection_name = config.get("DEFAULT", "collection_name")

# Initialize Firebase credentials
cred_path = os.path.join(base_dir, "cred", cred_fname)
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {"databaseURL": firebase_url})

# Initialize Flask & Swagger app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, send_wildcard=True)


# Swagger
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
@cross_origin()
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


# Define endpoint to add a new record to Firebase
@app.route("/api/record/", methods=["POST"])
@cross_origin()
@swag_from(post_dns_record_ep_doc)
def post_dns_record():
    data = request.data.decode("utf-8")
    data = json.loads(data)
    ref = db.reference("/")
    response = ref.update(data)
    return jsonify(response)


# Define endpoint to update a record from Firebase
@app.route("/api/record/<param>", methods=["PUT"])
@swag_from(put_dns_record_ep_doc)
def put_dns_record(param):
    param = "/".join(param.split(".")[::-1])
    data = request.data.decode("utf-8")
    data = json.loads(data)
    ref = db.reference(param)
    response = ref.update(data)
    return jsonify(response)


# Define endpoint to delete a record from Firebase
@app.route("/api/record/<param>", methods=["DELETE"])
@swag_from(delete_dns_record_ep_doc)
def delete_dns_record(param):
    param = "/".join(param.split(".")[::-1])
    ref = db.reference(param)
    response = ref.delete()
    return jsonify(response)


# Define endpoint to retrieve ip range of country from Firestore
@app.route("/api/global/<param>", methods=["GET"])
@swag_from(get_dns_global_ep_doc)
def get_global_range(param):
    db = firestore.client()
    docs = db.collection(collection_name).where("code", "==", param).stream()

    result = []
    for doc in docs:
        json = {"id": doc.id, **doc.to_dict()}
        result.append(json)

    return result


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
