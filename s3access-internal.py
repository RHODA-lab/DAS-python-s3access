import os
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
bucket_host = 'http://' + os.environ.get('BUCKET_HOST')
bucket_name = os.environ.get('BUCKET_NAME')

print("bucket_host:", bucket_host)
print("bucket_name:", bucket_name)
print("key_id:", key_id)
print("secret_key:", secret_key)
