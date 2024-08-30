
Our initial service framework is functional, but for production, we need to incorporate **model monitoring**, **version control**, and a **centralized model management system**. 

The current practice of deploying a new model instance on each node is not scalable. A more efficient approach would be to train the model once and then deploy it to a centralized serving node. This centralized node would be responsible for managing all trained models.

<p align="center">
    <img src = "../../docs/mlflow-simple-arch.png" style="width: 70%; "></img>
</p>