import boto3

def client():
    return boto3.client('ec2')

def start_instances():
    client = boto3.client('ec2')

response = client.start_instances(
    InstanceIds=[
        'string'
    ],
    DryRun=True|False,
)