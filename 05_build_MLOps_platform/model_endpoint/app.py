import os

import mlflow
from flask import Flask, jsonify, request

PORT = os.getenv("PORT", 9998)
SAMPLE_MODEL_NAME = "my_first_serving_model"

app = Flask(__name__)
model = None
mlflow.set_tracking_uri("http://tracking-server:5001")


@app.route("/change_model", methods=["POST", "GET"])
def load_latest_model():
    global model
    model_uri = f"models:/{SAMPLE_MODEL_NAME}@Champion"
    model = mlflow.transformers.load_model(model_uri)


load_latest_model()


@app.route("/predict", methods=["POST", "GET"])
def predict():
    data = request.get_json()
    input_data = data.get("input")
    prediction = model.predict(input_data)
    return jsonify(prediction)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=False)
