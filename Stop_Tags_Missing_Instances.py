import json
import boto3
import os

client = boto3.client('ec2')
sns_client = boto3.client('sns')
account = boto3.client('sts')


def lambda_handler(event, context):
    # TODO implement
    
    # Caputure EC2 start event trigger response
    get_instance_id=event['detail']['instance-id']
    
    response = client.describe_tags(
    Filters=[
        {'Name': 'resource-id',
        'Values': [get_instance_id]
        },
     ]
    )
    print(response)
    # Get all available TAGs
    all_tags = response['Tags']
    
    # Define action to stop TAGs missing instances
    action='STOP'
    for item in all_tags:
        print(item['Key'])
        if item['Key'] == 't_AppID':
            action='No_STOP'
            break
    print(action)
    
    if action == 'STOP':
        # Stop EC2
        response = client.stop_instances(InstanceIds=[get_instance_id])
        
        
        #Send SNS notification
        region = os.environ['AWS_REGION']
        accountid = account.get_caller_identity()['Account']
        sns_arn='arn:aws:sns:us-east-1:1234567890:EC2_Tag_Compliance'
        msg="EC2 instance (" + get_instance_id + ") Region " + region + " account " + accountid + " missing mandatory Tags and stopped"
        snsresponse = sns_client.publish(
            TopicArn=sns_arn,
            Message=msg,
            Subject="Mandatory Tags Policy Violated in " + accountid
            )