import os
import shutil

from flask import Flask, jsonify
from train import pipeline

PORT = os.getenv("PORT", 9999)

app = Flask(__name__)


@app.route("/train", methods=["POST", "GET"])
def train():
    result = pipeline()
    clear()
    return jsonify(result)


def clear():
    shutil.rmtree("/root/.cache/huggingface")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=False)
