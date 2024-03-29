import os
from google.cloud import storage

bucket_name = 'datawarehouse-04'
file_name = 'data.json'
local_dir_path = "/Users/macbookair/Documents/Arter/Data-Engineer-Bootcamp/Technical-Assignment/extract-load-demo/Task-1"
project_id = 'my_dataset'

storage_client = storage.Client(project=project_id)

bucket = storage_client.bucket(bucket_name)

for filename in os.listdir(local_dir_path):
    local_file_path = os.path.join(local_dir_path, filename)

    # Skip directories
    if os.path.isdir(local_file_path):
        continue

    blob = bucket.blob(file_name)
    blob.upload_from_filename(local_file_path)
    print(f"File {file_name} uploaded to {bucket_name} in GCS.")
