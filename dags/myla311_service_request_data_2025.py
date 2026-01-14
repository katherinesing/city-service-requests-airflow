import logging
from datetime import datetime

from airflow.sdk import dag, task

logger = logging.getLogger(__name__)


@dag(
    description="Upserts raw data for new or updated 2025 MyLA311 service requests https://dev.socrata.com/foundry/data.lacity.org/h73f-gn57",
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    end_date=datetime(2028, 12, 31),
    catchup=False,
)
def myla311_service_request_data_2025() -> None:

    @task
    def query_latest_data() -> None:
        logger.info("Fetching latest service request data for 2025")

    query_latest_data()


myla311_service_request_data_2025()
