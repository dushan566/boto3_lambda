# This will unallocate unattached Elastic IPs
import boto3

import boto3

# def lambda_handler(event, context):
#     client = boto3.client('ec2')
#     addresses_dict = client.describe_addresses()
#     for eip_dict in addresses_dict['Addresses']:
#         if "NetworkInterfaceId" not in eip_dict:
#             print(eip_dict['PublicIp'])
#             client.release_address(AllocationId=eip_dict['AllocationId'])

def lambda_handler():
    client = boto3.client('ec2', region_name='eu-west-1')
    addresses_dict = client.describe_addresses()
    for eip_dict in addresses_dict['Addresses']:
        if "NetworkInterfaceId" not in eip_dict:
            if "eipalloc-xxxxxxxxxxxxxx" in eip_dict.values(): #excludes a spesific EIP
                print("excluding " + eip_dict['AllocationId'] + "IP:" + eip_dict['PublicIp'])
            else:
                print("Deleting " + eip_dict['AllocationId'] + "IP:" + eip_dict['PublicIp'])
                client.release_address(AllocationId=eip_dict['AllocationId'])
