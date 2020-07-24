from pyspark.sql import SparkSession
from datetime import datetime


spark = SparkSession.builder.config("spark.jars.packages","org.apache.hadoop:hadoop-aws:2.7.0").getOrCreate()

input_path = ('s3://scripting-bucket/csv/test_data.csv')

df = spark.read.csv(input_path)

names = df.name.unique()

unique_last_name_list = set()

file = open('customer.txt', 'w')
file.write("\n" + 150*"=" + "\n")
file.write("\nScripting Starts at : " + str(datetime.now()) + "\n")
file.write("\n" + 150*"=" + "\n\n")


for name in names:
    split_name = name.split()
    last_name = split_name[len(split_name)-1]
    if last_name not in unique_last_name_list:
        unique_last_name_list.add(last_name)
        file.write(last_name+"\n")


file.write("\n" + 150*"=" + "\n")
file.write("\nScripting End at : " + str(datetime.now()) + "\n")
file.write("\n" + 150*"=" + "\n\n")
file.close()
