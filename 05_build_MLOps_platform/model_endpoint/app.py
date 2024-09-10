import logging
import os

import mlflow
from flask import Flask, jsonify, render_template_string, request

PORT = os.getenv("PORT", 9998)
SAMPLE_MODEL_NAME = "my_first_serving_model"

app = Flask(__name__)
model = None
mlflow.set_tracking_uri("http://tracking-server:5001")

toy_html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Prediction API</title>
</head>
<body>
    <h1>This is a toy example for flask api</h1>
    <form id="predictForm">
        <label for="inputData">Enter some text:</label>
        <input type="text" id="inputData" name="inputData">
        <button type="button" onclick="makePrediction()">Predict</button>
    </form>
    <h2>Prediction Result:</h2>
    <div id="result"></div>
    <script>
        function makePrediction() {
            var inputData = document.getElementById("inputData").value;
            fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ input: inputData }),
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("result").innerText = "Prediction: " + data.prediction;
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }
    </script>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(toy_html_template)


@app.route("/change_model", methods=["POST", "GET"])
def load_latest_model():
    global model
    try:
        model_uri = f"models:/{SAMPLE_MODEL_NAME}@Champion"
        model = mlflow.transformers.load_model(model_uri)
    except Exception as e:
        logging.info(e)
        model = lambda _: [{"result": "not found"}]


load_latest_model()


@app.route("/predict", methods=["POST", "GET"])
def predict():
    data = request.get_json()
    input_data = data.get("input")
    prediction = model(input_data)
    result = {"prediction": prediction}
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=False)
