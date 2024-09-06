# Machine-Learning-Model-Serving


To bridge the gap between model development and real-world application in machine learning, it's crucial to consider effective deployment strategies.

This article will concentrate on deploying machine learning models as services using **Python Flask APIs**, while also addressing key challenges and considerations commonly encountered in production environments.

The following topics will be discussed in this article:
- **How to build a model api by flask:** 
- **How to make a model api more robust:**
- **How to organize into microservices:**
- **How to monitor systems and models:**
- **How to build a machine learning CI/CD pipeline:**

Through a tour of 5 topics, we will build a service for an **MLOps** architecture, as shown below:

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


# uwsgi 安裝錯誤解
conda install uwsgi

