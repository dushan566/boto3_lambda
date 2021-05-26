import json, boto3

def lambda_handler(event, context):

    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('test-bucket-r')
       
    response = bucket.objects.delete()
    print(response)

    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
