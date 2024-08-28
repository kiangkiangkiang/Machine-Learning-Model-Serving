import os

from flask import Flask, jsonify, render_template_string, request
from toy_model import model

PORT = os.getenv("FLASK_PORT", 5001)

app = Flask(__name__)


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


@app.route("/predict", methods=["POST", "GET"])
def predict():
    data = request.get_json()
    input_data = data.get("input")
    prediction = model.predict(input_data)
    return jsonify(prediction)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
