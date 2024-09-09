Finally, we will use the previously mentioned **Nginx** and model endpoint as the model serving endpoint, and the **MLflow** server as the model version control and experiment monitoring endpoint. 

We will later add the **model training pipeline as an endpoint** for automating the training process. Additionally, we will manage the workflows of each node through **Airflow**, forming a complete automated platform for MLOps as shown below:

<p align="center">
    <img src = "../docs/mlops-arch.png" style="width: 100%; "></img>
</p>

## 1. MLflow Server

In the first step, we will set up an MLflow Server as the foundation for storing the models for the entire model serving process.

Similar to `04_model_tracking_and_monitoring`, we will use a comparable `docker-compose` configuration to set up the **MLflow** service, but we will make changes to the networking part:

```yaml
networks:
    mlops_network:
        driver: bridge
```

By setting up a common network `mlops_network`, all subsequent services will be able to communicate effectively.

## 2. Training Endpoint

By packaging the training pipeline into an **API** format, it will facilitate the automation of the training process in the future (if there are multiple machines, **GPU** resources can be assigned to this endpoint).

