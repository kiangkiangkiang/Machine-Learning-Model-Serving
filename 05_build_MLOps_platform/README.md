Finally, we will use the previously mentioned **Nginx** and model endpoint as the model serving endpoint, and the **MLflow** server as the model version control and experiment monitoring endpoint. 

We will later add the **model training pipeline as an endpoint** for automating the training process. Additionally, we will manage the workflows of each node through **Airflow**, forming a complete automated platform for MLOps shown as the following architecture:

<p align="center">
    <img src = "../docs/mlops-arch.png" style="width: 100%; "></img>
</p>
