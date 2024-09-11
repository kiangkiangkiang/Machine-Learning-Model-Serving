folders=("mlflow_server" "db" "training_endpoint" "model_endpoint" "airflow")

# 遍歷每個資料夔
for folder in "${folders[@]}"; do
  echo "Starting services in ${folder}..."
  (cd ${folder} && docker-compose up -d)
  
  if [ $? -ne 0 ]; then
    echo "Failed to start services in ${folder}"
  else
    echo "Services in ${folder} started successfully"
  fi
done

echo "All services started"