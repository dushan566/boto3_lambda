'''Terminate Instance
=================='''

import boto3

ec2 = boto3.resource('ec2')

instance_id = "i-040446b362b7486c8"
instance = ec2.Instance(instance_id)
response = instance.terminate()
print(response)