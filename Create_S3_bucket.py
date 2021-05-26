import json
import boto3

def lambda_handler(event, context):
    bucket_name = "my-test-bucket-2020abcd1234-sdsddasdaddfsdffe"
    s3 = boto3.resource('s3')
    response = bucket.create(
    Bucket=bucket_name,
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1'
    }
)

lambda_handler()
