import functools

import mlflow
from datasets import Dataset, DatasetDict, load_dataset
from model import *

mlflow.set_tracking_uri("http://localhost:5001")
SAMPLE_MODEL_NAME = "my_first_serving_model"


def load_model():
    try:
        model_uri = f"models:/{SAMPLE_MODEL_NAME}@Champion"
        model_artifact = mlflow.transformers.load_model(model_uri)
        return model_artifact.model, model_artifact.tokenizer
    except mlflow.exceptions.RestException as e:
        model, tokenizer = load_model_and_tokenizer()
        return model, tokenizer


def load_data():
    if False:
        # 連資料庫
        pass
    else:
        # 如果沒連到的話
        return load_dataset("imdb")


def send_msg():
    pass


def down_to_sample_data(dataset, n=1000):
    return DatasetDict(
        {
            "train": Dataset(dataset["train"].data[:n]),
            "test": Dataset(dataset["test"].data[:n]),
        }
    )


def mlflow_setup(exp_name="transformer-exp"):
    mlflow.set_tracking_uri("http://localhost:5001")
    client = mlflow.tracking.MlflowClient()
    if not mlflow.search_experiments(filter_string=f"name='{exp_name}'"):
        mlflow.create_experiment(name=exp_name)
    mlflow.set_experiment(experiment_name=exp_name)

    return client


def registry_model(client, results):
    try:
        client.get_model_version_by_alias(SAMPLE_MODEL_NAME, "Champion")

    except mlflow.exceptions.RestException as e:
        version = client.search_model_versions(f"name='{SAMPLE_MODEL_NAME}'")[0].version
        client.set_registered_model_alias(SAMPLE_MODEL_NAME, "Champion", version)
    finally:
        components = {
            "model": results.model,
            "tokenizer": results.tokenizer,
        }
        mlflow.transformers.log_model(
            transformers_model=components,
            artifact_path="transformers-model",
            registered_model_name=SAMPLE_MODEL_NAME,
        )


def pipeline():
    client = mlflow_setup()
    mlflow.autolog()
    model, tokenizer = load_model()
    dataset = load_data()
    dataset = down_to_sample_data(dataset)
    fun = functools.partial(preprocess_function, tokenizer)
    dataset = dataset.map(fun, batched=True)

    results = do_train(model, tokenizer, dataset)
    registry_model(client, results)

    print(123)


pipeline()
