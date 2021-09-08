import boto3
from botocore.exceptions import ClientError
import logging
import json

bucket_name = "my-test-bucket-2020abcd1234-sdsddasdaddfsdffe"
region = "eu-west-1"

def lambda_handler(event, context):
    try:
        s3 = boto3.resource('s3')
        response = s3.bucket.create(
        Bucket=bucket_name,
        ACL='private',
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    except ClientError as e:
        print("Something worng ", e)
        logging.error(e)
        
    finally:
        print("your bucket is ", response["Location"])

lambda_handler()
