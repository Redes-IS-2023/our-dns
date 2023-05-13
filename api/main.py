import base64
import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, jsonify

# Initialize Firebase credentials
cred = credentials.Certificate(
    "api/cred/our-dns-firebase-adminsdk-nmspx-f5917011e1.json"
)
firebase_admin.initialize_app(
    cred, {"databaseURL": "https://our-dns-default-rtdb.firebaseio.com"}
)

# Initialize Flask app
app = Flask(__name__)


# Define endpoint to retrieve data from Firebase
@app.route("/data/<param>", methods=["GET"])
def get_data(param):
    param = base64.b64decode(param).decode("utf-8")
    ref = db.reference(param)
    response = ref.get()

    # Return data as JSON response
    return jsonify(response)


# Run the app on localhost:5000
if __name__ == "__main__":
    app.run(debug=True)
