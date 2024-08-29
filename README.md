# Machine-Learning-Model-Serving


To bridge the gap between model development and real-world application in machine learning, it's crucial to consider effective deployment strategies.

This article will concentrate on deploying machine learning models as services using Python Flask APIs, while also addressing key challenges and considerations commonly encountered in production environments.

The following topics will be discussed in this article:
- **How to build a model api by flask:** 
  - Keywords: Flask, Transformers
- **How to make a model api more robust:**
  - Keywords: WSGI, Nginx, load balance
- **How to build a complete service system:**
  - Keywords: Docker, docker-compose
- **How to monitor systems and models:**
- **How to build a machine learning CI/CD pipeline:**
  - Keywords: CI/CD, MLOps, Training Pipeline & Deploy

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

