CREATE EXTENSION IF NOT EXISTS plpython3u;

-- Function to send HTTP request to Airflow, and return TRIGGER type
CREATE OR REPLACE FUNCTION trigger_airflow_dag()
RETURNS TRIGGER AS $$
import http.client
import json
import base64

host = "webserver"
port = 8080
path = "/api/v1/dags/machine-learning-training-pipeline/dagRuns"
username = "admin"
password = "admin"
auth_string = f"{username}:{password}"
base64_auth_string = base64.b64encode(auth_string.encode()).decode()

headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json",
    "Authorization": f"Basic {base64_auth_string}",
}

data = json.dumps({"conf": {}})

conn = http.client.HTTPConnection(host, port)
conn.request("POST", path, body=data, headers=headers)
response = conn.getresponse()

if response.status_code != 200:
    raise Exception("Failed to trigger DAG: " + response.text)

# Return the new row for the trigger to proceed
return "NEW"
$$ LANGUAGE plpython3u;

-- Trigger for INSERT and UPDATE
