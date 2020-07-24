import pandas as pd
import boto3
from datetime import datetime


access_key = your_s3_access_key
secret_access_key = your_s3_secret_access_key

s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)


bucket = "scripting-bucket"
file_name = "csv/test_data.csv"

obj = s3.get_object(Bucket=bucket, Key=file_name)

df = pd.read_csv(obj['Body'])

unique_last_name_list = set()

file = open('customer.txt', 'w')
file.write("\n" + 150*"=" + "\n")
file.write("\nScripting Starts at : " + str(datetime.now()) + "\n")
file.write("\n" + 150*"=" + "\n\n")

file2 = open('filtered_csv.txt', 'w')
file2.write("\n" + 150*"=" + "\n")
file2.write("\nScripting Starts at : " + str(datetime.now()) + "\n")
file2.write("\n" + 150*"=" + "\n\n")
file2.write("order_id,name,product_id,product_price" + "\n")

for row in df.itertuples():
    name = row.name
    split_name = name.split()
    last_name = split_name[len(split_name)-1]
    if last_name not in unique_last_name_list:
        unique_last_name_list.add(last_name)
        file.write(last_name+"\n")
        file2.write(str(row.order_id) + "," + str(row.name) + "," + str(row.product_id) + "," + str(row.product_price) + "\n")


file.write("\n" + 150*"=" + "\n")
file.write("\nScripting End at : " + str(datetime.now()) + "\n")
file.write("\n" + 150*"=" + "\n\n")
file.close()

file2.write("\n" + 150*"=" + "\n")
file2.write("\nScripting End at : " + str(datetime.now()) + "\n")
file2.write("\n" + 150*"=" + "\n\n")
file2.close()
