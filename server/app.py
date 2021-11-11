from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np


app = Flask(__name__)
CORS(app)


def generate_record(name):
    words = ["devil dog", "agile titan", "infinite ribbon",
             "virtual dancer", "muted biscuit", "bolo boot"]

    return {"codename": np.random.choice(words), "value": np.random.uniform(5, 15), "name": name}


@app.route("/search")
def search_name():

    print(request.args["name"])

    num_records = np.random.randint(5, 15)
    return jsonify([generate_record(request.args["name"]) for i in range(num_records)])


@app.route("/test")
def test():
    return jsonify(request.args["name"]+"FLASKED")


if __name__ == "__main__":

    app.run(debug=True)
