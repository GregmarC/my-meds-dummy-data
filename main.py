from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/1", methods=["GET", "OPTIONS"])
def get_example():
    """GET in server"""
    response = jsonify(data={"meds" : ["tylenol", "advil", "motrin"]})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/", methods=["POST"])
def post_example():
    """POST in server"""
    return jsonify(message="POST request returned")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)