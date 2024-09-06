from transformers import pipeline


class ToyModel:
    def __init__(self):
        self.classifier = pipeline(
            "sentiment-analysis", model="stevhliu/my_awesome_model"
        )

    def predict(self, input_data):
        output = self.classifier(input_data)
        output = self.classifier(input_data)[0]
        return {
            "prediction": "Scores: "
            + str(output["score"])
            + "\n"
            + "Label: "
            + output["label"]
        }


model = ToyModel()
