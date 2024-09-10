CREATE EXTENSION IF NOT EXISTS plpython3u;

-- Function to send HTTP request to Airflow, and return TRIGGER type
CREATE OR REPLACE FUNCTION trigger_airflow_dag()
RETURNS TRIGGER AS $$
import requests
import base64

# Airflow webserver URL 和 DAG ID
airflow_url = "http://webserver:8080/api/v1/dags/machine-learning-training-pipeline/dagRuns"
username = "admin"
password = "admin"
auth_string = f"{username}:{password}"
encoded_auth = base64.b64encode(auth_string.encode()).decode()

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {encoded_auth}"
}

response = requests.post(airflow_url, headers=headers)
if response.status_code != 200:
    raise Exception("Failed to trigger DAG: " + response.text)

# Return the new row for the trigger to proceed
return "NEW"
$$ LANGUAGE plpython3u;

-- Trigger for INSERT and UPDATE
CREATE TRIGGER imdb_train_notify
AFTER INSERT OR UPDATE ON imdb_train
FOR EACH ROW EXECUTE FUNCTION trigger_airflow_dag();