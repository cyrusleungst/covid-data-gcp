from google.cloud import storage
from google.oauth2 import service_account
from datetime import datetime

GOOGLE_APPLICATION_CREDENTIALS = "amiable-wonder-329721-0e439cdcc354.json"
SERVICE_ACCOUNT_JSON = r"amiable-wonder-329721-0e439cdcc354.json"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_JSON, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
bucket_name = "cyrus-covid-bucket"

client = storage.Client(credentials=credentials, project=credentials.project_id)

today = datetime.today().strftime('%Y-%m-%d')

def upload_to_bucket(blob_name, file_path, bucket_name):
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)
    print(f"{blob_name} uploaded to {bucket_name} successfully")
    return True

upload_to_bucket(f"{today}.json", f"{today}.json", "cyrus-covid-bucket")
