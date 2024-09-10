import functools
import gc
import logging
import os

import dotenv
import mlflow
import pandas as pd
from datasets import Dataset, DatasetDict, load_dataset
from huggingface_hub import login
from model import *
from sqlalchemy import create_engine, inspect

dotenv.load_dotenv()
mlflow.set_tracking_uri(
    "http://tracking-server:5001"
)  # Use docker network to connect tracking-server. Or you can use ip as well.
logging.basicConfig(level=logging.INFO)
SAMPLE_MODEL_NAME = "my_first_serving_model"
SLACK_URL = os.environ.get("SLACK_URL", None)
db_engine = create_engine(
    "postgresql+psycopg2://mlops:mlops@training-database:5432/imdb_db"
)  # Use docker network to connect training-database. Or you can use ip as well.


def load_model():
    try:
        model_uri = f"models:/{SAMPLE_MODEL_NAME}@Champion"
        model_pipeline = mlflow.transformers.load_model(model_uri)
        return model_pipeline.model, model_pipeline.tokenizer
    except mlflow.exceptions.RestException as e:
        model, tokenizer = load_model_and_tokenizer()
        return model, tokenizer


def load_data():
    def save_to_db(dataset, split, table_name):
        df = pd.DataFrame(dataset[split])
        df.to_sql(table_name, db_engine, index=False, if_exists="replace")

    def fetch_from_db(table_name):
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, db_engine)
        return df

    all_tables = inspect(db_engine).get_table_names()

    if "imdb_train" in all_tables and "imdb_test" in all_tables:
        logging.info("Found data in database. Fetching the data...")
        train = Dataset.from_pandas(fetch_from_db("imdb_train"))
        test = Dataset.from_pandas(fetch_from_db("imdb_test"))
        return DatasetDict(
            {
                "train": train,
                "test": test,
            }
        )
    else:
        logging.info("Data not found in database. Initialize a new dataset...")
        dataset = load_dataset("imdb")
        save_to_db(dataset, "train", "imdb_train")
        save_to_db(dataset, "test", "imdb_test")
        return dataset


def send_msg(payload, slack_webhook_url):
    """Use Slack Webhook to send result message to data scientist in pre-registered slack channel"""

    if not slack_webhook_url:
        return

    import json

    import urllib3

    http = urllib3.PoolManager()
    try:
        http.request("POST", slack_webhook_url, body=json.dumps({"text": payload}))
    except Exception as e:
        logging.info(e)


def down_to_sample_data(dataset, n=1000):
    """Produce the sample data"""

    return DatasetDict(
        {
            "train": Dataset(dataset["train"].data[:n]),
            "test": Dataset(dataset["test"].data[:n]),
        }
    )


def compare_performance(current_eval_results, champion_eval_results):
    """For the sample case, we will not do anything in this function.
    User can customize how to compare and how to decide to change "Champion" alias.
    """

    return True


def set_alias_for_current_model(client, alias):
    version = client.search_model_versions(f"name='{SAMPLE_MODEL_NAME}'")[0].version
    client.set_registered_model_alias(SAMPLE_MODEL_NAME, alias, version)


def registry_model(client, results):
    # Registry The Latest Model
    components = {
        "model": results.model,
        "tokenizer": results.tokenizer,
    }
    mlflow.transformers.log_model(
        task="text-classification",
        transformers_model=components,
        artifact_path="transformers-model",
        registered_model_name=SAMPLE_MODEL_NAME,
    )

    # Compare to the champion version
    try:
        champion_version = client.get_model_version_by_alias(
            SAMPLE_MODEL_NAME, "Champion"
        )
        champion_performance = client.get_run(champion_version.run_id).data.metrics
        if compare_performance(results.state.log_history[0], champion_performance):
            set_alias_for_current_model(client, "Champion")
    except mlflow.exceptions.RestException as e:
        set_alias_for_current_model(client, "Champion")


def pipeline():
    # Huggingface Setup
    login(token=os.environ.get("HUGGINGFACE_TOKEN"))

    # MLflow Setup
    client = mlflow.tracking.MlflowClient()
    exp_name = "transformer-exp"
    if not mlflow.search_experiments(filter_string=f"name='{exp_name}'"):
        mlflow.create_experiment(name=exp_name)
    mlflow.set_experiment(experiment_name=exp_name)

    # Training Pipeline
    logging.info("Load Model...")
    model, tokenizer = load_model()

    logging.info("Load Data...")
    dataset = load_data()
    dataset = down_to_sample_data(dataset)
    fun = functools.partial(preprocess_function, tokenizer)
    dataset = dataset.map(fun, batched=True)

    logging.info("Start Training...")
    with mlflow.start_run():
        results = do_train(model, tokenizer, dataset)

        # Register model
        logging.info("Register Model...")
        registry_model(client, results)

    # Send Message
    send_msg(
        f"eval_loss: {results.state.log_history[0]['eval_loss']}, eval_accuracy: {results.state.log_history[0]['eval_accuracy']}",
        SLACK_URL,
    )

    del model, tokenizer, dataset, results
    gc.collect()

    return "Success"
