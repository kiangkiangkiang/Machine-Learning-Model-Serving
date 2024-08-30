
Our initial service framework is functional, but for production, we need to incorporate **model monitoring**, **version control**, and a **centralized model management system**. 

The current practice of deploying a new model instance on each node is not scalable. A more efficient approach would be to train the model once and then deploy it to a centralized serving node. This centralized node would be responsible for managing all trained models.

<p align="center">
    <img src = "../../docs/mlflow-simple-arch.png" style="width: 70%; "></img>
</p>

By leveraging **MLflow**, we can effortlessly manage our models. This means we can directly **pull specific versions of models to our model endpoints** for serving (as shown in the figure). 

Furthermore, this framework facilitates model iteration and subsequent automation processes such as deployment.

## Build MLflow Services - Simply

Install `mlflow` package
```bash
pip install mlflow
```

We now can quick launch a mlflow server by the following command:
```bash
mlflow server --host 0.0.0.0 --port 5001
```

See command the details: https://mlflow.org/docs/latest/cli.html

## Build MLflow Services - Docker Compose

Through the tours of `03_docker_compose_services`, we know how to construct services by `docker-compose`. Thus, instead of building all components in the same container (simply demo), we are going to use `docker-compose` to build the `mlflow` architecture above.

TODO
```
docker-compose here
```

## Services Quick Tour

### Experiments

### Serving


python:3.10.14-bookworm

## Reference
- [mlflow document](https://mlflow.org/docs/latest/index.html)
- [mlflow docker setup](https://github.com/PenHsuanWang/mlflow-docker-setup)
