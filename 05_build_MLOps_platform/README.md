Finally, we will use the previously mentioned **Nginx** and model endpoint as the model serving endpoint, and the **MLflow** server as the model version control and experiment monitoring endpoint. 

We will later add the **model training pipeline as an endpoint** for automating the training process. Additionally, we will manage the workflows of each node through **Airflow**, forming a complete automated platform for MLOps as shown below:

<p align="center">
    <img src = "../docs/mlops-arch.png" style="width: 100%; "></img>
</p>

Hereafter, I will explain how to compose the aforementioned ML framework using five main components.

## 1. MLflow Server

In the first step, we will set up an **MLflow** Server as the foundation for storing the models for the entire model serving process.

Similar to `04_model_tracking_and_monitoring`, we will use a comparable `docker-compose` configuration to set up the **MLflow** service.

It is worth mentioning that this is the first service we establish; therefore, to ensure smooth communication with subsequent services, the network settings of other services will be configured to match this service.

By default, `docker-compose` uses the name `{PRJT_NAME}_default` for the default network, but in this instance, it will be `mlflow_server_default`.

## 2. Training Endpoint

By packaging the training pipeline into an **API** format, it will facilitate the automation of the training process in the future (if there are multiple machines, **GPU** resources can be assigned to this endpoint).

### Set Environment

Before setting up this service, please ensure that there is a `./training_endpoint/.env` file in the folder. Edit it as follows:

```yaml
SLACK_URL = "YOUR_SLACK_WEBHOOK_URL" # If there is no webhook, leave it empty is ok.
HUGGINGFACE_TOKEN = "YOUR_HUGGINGFACE_TOKNE" # huggingface access token
```

The main settings include the message link for **training results (optional)** and the **Hugging Face access token (required)**.

### Training Pipeline

This example primarily demonstrates how to train a **text classification model** with **huggingface framework**. However, under the current topic, we will not delve deeply into model training but will instead focus more on service establishment.

You can find the complete training pipeline in `./training_endpoint/train.py`, while `./training_endpoint/model.py` contains the relevant training configurations from the **Huggingface** documentation [here](https://huggingface.co/docs/transformers/tasks/sequence_classification).

It is worth mentioning that we have built this training pipeline into an **API** and deployed the service using `docker-compose`. The specially configured **docker-compose.yaml** file is as follows:

```yaml
networks:
    - your_mlflow_network
deploy:
    resources:
        reservations:
            devices:
                - capabilities: [gpu]
```

To enable **NVIDIA** support, the following configuration is needed in the **docker-compose.yaml** file to declare **hardware devices** and configure the **network** to the same area as **MLflow**. This way, effective communication with the **MLflow** server can be established.

## 3. Training Database

To recap, our service aims to automatically trigger the training process when new data is added and seamlessly switch to the latest version of the model as a service. 

**Thus, this phase primarily involves setting up our training database and writing the Trigger into the internal database.** When the **Trigger** is activated, we plan to invoke the **Airflow** service to manage the entire workflow, which is look like:

<p align="center">
    <img src = "../docs/airflow-workflow.png" style="width: 70%; "></img>
</p>


For more details, please refer to the `./db` folder.

## 4. Model Endpoint

## 5. Airflow


# Quickstart 

TODO