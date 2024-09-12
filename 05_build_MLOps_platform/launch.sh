#!/bin/sh

folders="mlflow_server db training_endpoint model_endpoint airflow"

for folder in $folders; do
  echo "Starting services in ${folder}..."
  
  if [ -d "${folder}" ]; then
    (cd "${folder}" && docker-compose up -d)
    if [ $? -ne 0 ]; then
      echo "Failed to start services in ${folder}"
    else
      echo "Services in ${folder} started successfully"
    fi
  else
    echo "Folder ${folder} does not exist"
  fi
done

echo "All services started"