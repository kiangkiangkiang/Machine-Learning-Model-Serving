# Full-Stack Automated Machine Learning Model Serving

In this article, we aim to discuss how to build a comprehensive **local model services**. Unlike previously using AWS services at **[AWS-Sagemaker-Face-Detection-Example](https://github.com/kiangkiangkiang/AWS-Sagemaker-Face-Detection-Example)**, here we manually set up the complete service using **Docker**.

The setup of all services will primarily **focus on the skills of Data Scientists and Machine Learning Engineers**. We will not delve deeply into topics from other domains. The final comprehensive framework is as follows.

<p align="center">
    <img src = "./docs/mlops-arch.png" style="width: 80%; "></img>
</p>

Through the introduction in the following chapters, we will step-by-step to build a simple yet practical service, or you can go directly to `./05_build_MLOps_platform` to use the final service.

## Serving Model Endpoints

We first discussed how to set up a very simple model service using **Flask API** in `./01_build_model_endpoint_by_flask`, where the model is directly pulled from **Huggingface**. If you are interested in building a language model, you can refer to **[Text Information Extraction](https://github.com/kiangkiangkiang/Information-Extraction-for-Chinese-NLP)**. We will not delve into the modeling details but rather focus on the overall framework.

Next, in sections `./02_flask_api_with_nginx_and_wsgi` and `./03_docker_compose_services`, we will discuss in detail how to distribute traffic to multiple model endpoints, i.e., **Load Balance**. Therefore, we will talk about how to set up **Nginx & WSGI**, and how to package the entire service using **docker-compose**.

## Model and Experiment Monitoring

In the Machine Learning lifecycle, the models in the service often need to be iterated (data updates or model updates). Therefore, the concept of **Model Registry** becomes very important. 

In `./04_model_tracking_and_monitoring`, we will discuss how to set up an on-premise **MLflow** Server to manage all model versions and experiment versions. During the learning process, we will manually set up a **custom backend database** and **model artifact**. 

### Airflow Management

During the model service phase, we have many steps that require automation, such as automated training, automated model updating, and so on. To manage this automation process, we introduced **Airflow** services to control the entire workflow.

It is usually considered a **scheduling management tool**, but with some special configurations, it can also function as an **API-triggered** script (See `./05_build_MLOps_platform`). This way, we can ultimately achieve automated triggering of our machine learning pipeline.

## Reference
- [MLflow Document](https://mlflow.org/docs/latest/index.html)
- [MLflow Docker Setup](https://github.com/PenHsuanWang/mlflow-docker-setup)
- [MLflow with Remote Tracking Server, Backend and Artifact Stores](https://medium.com/lionswerk/mlflow-with-remote-tracking-server-backend-and-artifact-stores-39912680a464)
- [WSGI Basic Concept](https://minglunwu.com/notes/2021/flask_plus_wsgi.html/)
- [Flask with Nginx & WSGI](https://medium.com/%E5%B7%A5%E7%A8%8B%E9%9A%A8%E5%AF%AB%E7%AD%86%E8%A8%98/flask-app-%E5%8A%A0%E4%B8%8A-wsgi-%E5%8F%8A-nginx-%E6%9C%8D%E5%8B%99-b8bdc60d1dc7)
- [Forward Proxy & Reverse Proxy](https://www.pressplay.cc/project/F720CEB1D6057D7ABB5614722AB18FFF/articles/660A57208C29FF94453548ED21F284EF)
- [Load Testing Tool](https://loader.io/)
- [uWSGI & Nginx](https://hackmd.io/@luluxiu/By2ZsccgT)
