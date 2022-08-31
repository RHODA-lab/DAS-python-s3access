import os
import sys
import requests
import json
import time
import logging
import random
import pandas as pd
import boto3
from boto3 import session

key_id = os.environ.get('AWS_ACCESS_KEY_ID')
secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
bucket_host = os.environ.get('BUCKET_HOST')
bucket_name = os.environ.get('BUCKET_NAME')
if (key_id is None or secret_key is None or bucket_host is None or bucket_name is None):
  sys.exit('Environment variable with Object Bucket Claim info has not been set')

bucket_host = 'http://' + bucket_host
s3 = boto3.client('s3','', endpoint_url= bucket_host,
    aws_access_key_id = key_id,
    aws_secret_access_key = secret_key)

for x in s3.list_buckets()['Buckets']:
  current_bucket = x['Name']
  print("----Objects in Bucket: ", current_bucket)
  for object in s3.list_objects(Bucket=current_bucket)['Contents']:
    print(object['Key'], str(object))

"""
# For creating an object called "junk_object1" with some random data
s3.put_object(Bucket=bucket_name,Key='junk_object1',Body='hello world 11111111')
"""

