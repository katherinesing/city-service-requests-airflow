# About
Process raw data for city service requests

# Setup
To create necessary folders not already in the repo \
```mkdir -p ./logs ./plugins ./config```

To add an airflow user necessary for the next step \
```echo -e "AIRFLOW_UID=$(id -u)" > .env```

To run database migrations and create the first user account \
```docker compose up airflow-init``` \
you should see this result: airflow-init-1 exited with code 0

To start the airflow cluster \
```docker compose up -d``` \
When cluster is up, go to http://localhost:8080 \
username: airflow \
password: airflow \
```ctrl + c``` to exit 

To stop and delete containers, delete volumes with database data and download images \
```docker compose down --volumes --rmi all```