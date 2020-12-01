from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/1", methods=["GET", "OPTIONS"])
def get_example():
    """GET in server"""
    response = jsonify(data={"meds" : [{"medName":"Tylenol 500 mg", "directions":"Once a day, Everyday, 60 tablets", "refill":"11/30/21","exp":"12/31/22", "image":"https://www.meijer.com/content/dam/meijer/product/0030/04/5044/90/0030045044905_2_A1C1_0600.png"}, {"medName":"Advil 200 mg", "directions":"Twice a day, before breakfast and before dinner, 60 tablets", "image":"https://images.heb.com/is/image/HEBGrocery/000231870", "refill":"11/30/21", "exp":"1/31/22"}, {"medName":"Metformin 500 mg", "refill":"12/31/20", "exp":"12/31/21", "directions": "Once a day with breakfast, everyday, 30 tablets", "image":"https://res.cloudinary.com/grohealth/image/upload/$wpsize_!post-thumbnail!,w_1000,h_600,c_fill,g_auto/v1588088500/Metformin-1200x630-1.jpg"}], "name" : "Greg Cruz", "age" : "31"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/", methods=["POST"])
def post_example():
    """POST in server"""
    return jsonify(message="POST request returned")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)