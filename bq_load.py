from google.cloud import bigquery
from google.oauth2 import service_account
from datetime import datetime

SERVICE_ACCOUNT_JSON = r"amiable-wonder-329721-0e439cdcc354.json"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_JSON, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

today = datetime.today().strftime('%Y-%m-%d')

table_id = f"amiable-wonder-329721.covid.{today}"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("Country", "STRING"),
        bigquery.SchemaField("CountryCode", "STRING"),
        bigquery.SchemaField("NewConfirmed", "INTEGER"),
        bigquery.SchemaField("TotalConfirmed", "INTEGER"),
        bigquery.SchemaField("NewDeaths", "INTEGER"),
        bigquery.SchemaField("TotalDeaths", "INTEGER"),
        bigquery.SchemaField("Date", "DATE"),
    ],
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
)

uri = f"gs://cyrus-covid-bucket/{today}.json"

load_job = client.load_table_from_uri(
    uri,
    table_id,
    location="europe-west2",
    job_config=job_config,
)

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)
print("Loaded {} rows.".format(destination_table.num_rows))