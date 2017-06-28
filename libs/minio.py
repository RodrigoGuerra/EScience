import os

from minio import Minio

client = Minio(os.environ['MINIO_URL'],
               access_key=os.environ['MINIO_ACCESS_KEY'],
               secret_key=os.environ['MINIO_SECRET_KEY'],
               secure=False)
bucket = "my-scripts"
