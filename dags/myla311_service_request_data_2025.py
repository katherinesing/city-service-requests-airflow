import logging
import os
from dotenv import load_dotenv
from sodapy import Socrata
from datetime import datetime, timedelta

from airflow.sdk import dag, task, get_current_context

logger = logging.getLogger(__name__)

# Load environment variables from the .env file
load_dotenv()

socrata_domain = os.getenv("SOCRATA_DOMAIN")
socrata_dataset_identifier = os.getenv("SOCRATA_DATASET_IDENTIFIER")
socrata_app_token = os.getenv("SOCRATA_APP_TOKEN")


@dag(
    description="Upserts raw data for new or updated 2025 MyLA311 service requests https://dev.socrata.com/foundry/data.lacity.org/h73f-gn57",
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    end_date=datetime(2028, 12, 31),
    catchup=False,
    # default_args={"retries": 4},  # Retry up to 4 times on failure (e.g. API timeouts)
)
def myla311_service_request_data_2025() -> None:

    @task
    def query_latest_data() -> None:
        logger.info("Fetching latest service request data for 2025")

        context = get_current_context()
        start_date = context["data_interval_start"].strftime("%Y-%m-%dT00:00:00.000")
        end_date = context["data_interval_end"].strftime("%Y-%m-%dT00:00:00.000")

        logger.info(
            f"Data interval: {context["data_interval_start"]} to {context["data_interval_end"]}"
        )
        logger.info(f"Start, end dates: {start_date} to {end_date}")

        # Socrata Query Language (SoQL)
        query = f"""
            select
                *
            where
                (createddate >= "{start_date}"
                and createddate < "{end_date}")
                or (
                    createddate < "{start_date}"
                    and updateddate >= "{start_date}"
                    and updateddate < "{end_date}"
                )
        """

        client = Socrata(socrata_domain, socrata_app_token)
        results = client.get(socrata_dataset_identifier, query=query)
        logger.info(f"Fetched {len(results)} records")

    query_latest_data()


myla311_service_request_data_2025()
