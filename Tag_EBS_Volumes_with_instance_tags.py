import boto3


## mapping each volume to its attached instance and filter out unattached instances
def get_vol_ins_map(client):
    response = client.describe_volumes()

    vol_ins_map = list()
    not_attached = list()



    for volume in response['Volumes']:
        if volume['Attachments']:
            if len(volume['Attachments']) > 1:
                print('more than 1 attachments')  # Not valid for EBS
            else:
                # print('has only one attachments  ' , volume['VolumeId'] , "  " , volume['Attachments'][0]['InstanceId'])
                vol_ins_map.append({volume['VolumeId']: volume['Attachments'][0]['InstanceId']})
        else:
            # print ('Not attached ' + volume['VolumeId'])
            not_attached.append(volume['VolumeId'])
    return (vol_ins_map, not_attached)


## reading instance tags and extracting only desired tags    
def read_and_filter_tags(client, ins_id):
    response = client.describe_instances(
        InstanceIds=[ins_id]
    )

    tags = (response['Reservations'][0]['Instances'][0]['Tags'])

    exteracted_tags = list()
    for tag_key in ['Name', 't_cost_centre', 't_dcl', 't_AppID', 't_environment']:
        try:
            exteracted_tags.append(next(item for item in tags if item["Key"] == tag_key))
        except Exception as e:
            exteracted_tags.append({'Key': tag_key, 'Value': ''})
            print(e)
    return exteracted_tags


## tagging the resource
def tag_resource(client, vol_id, tag_list):
    response = client.create_tags(
        Resources=[vol_id],
        Tags=tag_list
    )


def lambda_handler(event, context):
    #aws_region = event['region']
    client = boto3.client('ec2', 'eu-west-1')
    volume_ins_map, unattached_vol = get_vol_ins_map(client)

    tagged_volumes = list()
    for item in volume_ins_map:
        for value in item.values():
            inst_id = value
            result_tag_list = (read_and_filter_tags(client, inst_id))
            for key in item.keys():
                tag_resource(client, key, result_tag_list)
                tagged_volumes.append(key)
        
        #remove this break line if everything is ok
        #break  

    print('-----tagged volumes-------')
    print(tagged_volumes)
    print('------------end---------------\n')

    print('-----unattached volumes-------\n')
    print(unattached_vol)
    print('------------end---------------')