import base64
import firebase_admin
from firebase_admin import credentials, db
from flasgger import Swagger, swag_from
from flask import Flask, jsonify
from swagger_doc.doc import testing_ep_doc


# Initialize Firebase credentials
cred = credentials.Certificate(
    "api/cred/our-dns-firebase-adminsdk-nmspx-f5917011e1.json"
)
firebase_admin.initialize_app(
    cred, {"databaseURL": "https://our-dns-default-rtdb.firebaseio.com"}
)

# Initialize Flask & Swagger app
app = Flask(__name__)
swagger = Swagger(app)


# Define endpoint to retrieve data from Firebase
@app.route("/api/testing/<param>", methods=["GET"])
@swag_from(testing_ep_doc)
def get_data(param):
    try:
        param = base64.b64decode(param).decode("utf-8")
    except:
        return jsonify({"error": "Invalid parameter."}), 400

    ref = db.reference(param)
    response = ref.get()

    return jsonify(response)


# Run the app on localhost:5000
if __name__ == "__main__":
    app.run(debug=True)
