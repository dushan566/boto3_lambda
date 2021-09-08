import boto3
import datetime
client = boto3.client('ec2',region_name='eu-west-1')

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name='eu-west-1')
    # Get list of snapshots own by you
    snapshots = client.describe_snapshots(OwnerIds=['1234567890'])
    for snapshot in snapshots['Snapshots']:
        a= snapshot['StartTime']
        b=a.date()
        c=datetime.datetime.now().date()
        d=c-b
        ## Delete snapshots older than 2 days
        try:
            if d.days>2:
                id = snapshot['SnapshotId']
                client.delete_snapshot(SnapshotId=id)
        # Skip in use snapshots        
        except Exception as e:
            if 'InvalidSnapshot.InUse' in e.message:
                print("skipping snapshot", e)
                continue