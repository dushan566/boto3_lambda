import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name='eu-west-1')
    #List unattached volumes
    volumes = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['available']}])
    
    #Delete Unattached Volumes
    for v in volumes:
        print(v.id)
        response = v.delete(
            DryRun=False
            )