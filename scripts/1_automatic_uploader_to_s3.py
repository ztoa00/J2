import boto3
import os


access_key = your_s3_access_key
secret_access_key = your_s3_secret_access_key

client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)


for file in os.listdir():
    if file == 'test_data.csv':
        upload_file_bucket = 'scripting-bucket'
        upload_file_key = 'csv/' + str(file)
        print(upload_file_key)
        client.upload_file(file, upload_file_bucket, upload_file_key)
