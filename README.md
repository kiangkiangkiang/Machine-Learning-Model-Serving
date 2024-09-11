# Full-Stack Automated Machine Learning Pipeline

This article will concentrate on deploying machine learning models as services using **Flask API, Nginx, WSGI, MLflow, Airflow**, to build a ML pipeline such as the following architecture. While also addressing key challenges and considerations commonly encountered in production environments.

<p align="center">
    <img src = "./docs/mlops-arch.png" style="width: 100%; "></img>
</p>


Through the introduction in the following chapters, we will build a simple yet practical ML Pipeline. It will achieve among other common ML-related services:
- **Automatic Model Iteration/Development**
- **Automated Model Training**
- **Experiment Monitoring**
- **Traffic Control**
- **Workflow and Trigger Management**

## Serving Model Endpoints

## Scaling with Load Balancer

## Model and Experiment Monitoring

## Model and Experiment Monitoring


**MLflow** is one of the most important services for tracking models, experiments, and more during the training process. 

Therefore, during the learning process, we will manually set up the **MLflow** service, as well as create a **custom backend database** and **model storage**. The schematic diagram is as follows:



### Airflow


