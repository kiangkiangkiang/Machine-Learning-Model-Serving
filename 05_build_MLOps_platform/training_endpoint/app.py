import os

from flask import Flask, jsonify
from train import pipeline

PORT = os.getenv("PORT", 9999)

app = Flask(__name__)


@app.route("/train", methods=["POST", "GET"])
def predict():
    result = pipeline()
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
