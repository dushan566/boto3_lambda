import boto3
import datetime
client = boto3.client('ec2',region_name='eu-west-1')

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name='eu-west-1')
    snapshots = client.describe_snapshots(OwnerIds=['266665223494'])
    for snapshot in snapshots['Snapshots']:
        a= snapshot['StartTime']
        b=a.date()
        c=datetime.datetime.now().date()
        d=c-b
        try:
            if d.days>2:
                id = snapshot['SnapshotId']
                client.delete_snapshot(SnapshotId=id)
        except Exception as e:
            if 'InvalidSnapshot.InUse' in e.message:
                print("skipping snapshot", e)
                continue