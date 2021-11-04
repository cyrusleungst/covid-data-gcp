from google.cloud import bigquery
from google.oauth2 import service_account

SERVICE_ACCOUNT_JSON = r"amiable-wonder-329721-0e439cdcc354.json"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_JSON, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

dataset_id = "amiable-wonder-329721.covid"

dataset = bigquery.Dataset(dataset_id)

dataset.location = "europe-west2"
dataset.description = "dataset to store covid data"

dataset_ref = client.create_dataset(dataset, timeout=30)

print(f"Dataset {client.project}.{dataset_ref.dataset_id} has been created")

