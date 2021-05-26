# This will unallocate unattached Elastic IPs
import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2')
    addresses_dict = client.describe_addresses()
    for eip_dict in addresses_dict['Addresses']:
        if "NetworkInterfaceId" not in eip_dict:
            print(eip_dict['PublicIp'])
            client.release_address(AllocationId=eip_dict['AllocationId'])