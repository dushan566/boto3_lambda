'''Launch Instance
#==============='''
import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-07683a44e80cd32c5',
    MinCount=1,
    MaxCount=1,
    SubnetId='subnet-c0acac98',
    InstanceType='t2.micro')

# Another way
#ec2.create_instances(ImageId='<ami-image-id>', MinCount=1, MaxCount=5)

print(instance[0].id)