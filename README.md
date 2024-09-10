# Machine-Learning-Model-Serving

To bridge the gap between model development and real-world application in machine learning, it's crucial to consider effective deployment strategies.

This article will concentrate on deploying machine learning models as services using **Python Flask APIs**, while also addressing key challenges and considerations commonly encountered in production environments.

The following topics will be discussed in this article:
- **How to build a model api by Flask:** 
- **How to build a load balancer by Nginx for model endpoints:**
- **How to organize into microservices:**
- **How to use mlflow monitor and control model version:**
- **How to automate ML pipeline with Airflow:**

Through a tour of **5 topics**, we will build a service for an **MLOps** architecture, as shown below:

<p align="center">
    <img src = "./docs/mlops-arch.png" style="width: 100%; "></img>
</p>

## System Setup 

Our system is configured to the following specifications:

- **python 3.10**
- **ubuntu 22.04**
- **docker-compose 2.29.2**

For the `docker-compose` package. It can be installed by the following command:
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Use `docker-compose --version` to check your version:

The services we will be using next will mostly run in a **Docker** environment, so you can refer to the settings in the `Dockerfile` or `docker-compose.yaml` for most of the services.

## Services Integration

### MLflow

**MLflow** is one of the most important services for tracking models, experiments, and more during the training process. 

Therefore, during the learning process, we will manually set up the **MLflow** service, as well as create a **custom backend database** and **model storage**. The schematic diagram is as follows:

<p align="center">
    <img src = "./docs/mlflow-server.png" style="width: 100%; "></img>
</p>

### Airflow


