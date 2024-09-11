import base64

import requests
from requests.auth import HTTPBasicAuth

username = "admin"
password = "admin"

auth_string = f"{username}:{password}"
base64_auth_string = base64.b64encode(auth_string.encode()).decode()
print(base64_auth_string)

# url = 'http://x.x.x.x:8080/api/v1/dags/{dag_id}/dagRuns'
url = "http://localhost:8080/api/v1/dags/machine-learning-training-pipeline/dagRuns"

headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json",
    "Authorization": f"Basic {base64_auth_string}",
}

data = {"conf": {}}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.text)
