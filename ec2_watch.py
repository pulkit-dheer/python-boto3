import boto3


ec2_client = boto3.client('ec2', region_name="ap-south-1")
ec2_resource = boto3.resource('ec2', region_name="ap-south-1")


reservations = ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    instances = reservation["Instances"]
    for instance in instances:
        print(f"Instance {instance['InstanceId']} is {instance['State']['Name']}")

