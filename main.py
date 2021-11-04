from datetime import datetime
from google.cloud import bigquery

today = datetime.today().strftime('%Y-%m-%d')

def load_to_bq(event, context):
    file = event
    table_id = f"amiable-wonder-329721.covid.{today}"
    uri = f"gs://cyrus-covid-bucket/{today}.json"

    print(f"Processing file: {file['name']}, {file['timeCreated']}.")

    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig()
    job_config.schema = [bigquery.SchemaField("Country", "STRING"),bigquery.SchemaField("CountryCode", "STRING"),bigquery.SchemaField("NewConfirmed", "INTEGER"),bigquery.SchemaField("TotalConfirmed", "INTEGER"),bigquery.SchemaField("NewDeaths", "INTEGER"),bigquery.SchemaField("TotalDeaths", "INTEGER"),bigquery.SchemaField("Date", "DATE"),]
    job_config.source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,

    load_job = client.load_table_from_uri(uri,table_id,location="europe-west2",job_config=job_config,)
    load_job.result()  # Waits for the job to complete.
    destination_table = client.get_table(table_id)
    
    print(f"Loaded {destination_table.num_rows} rows.")