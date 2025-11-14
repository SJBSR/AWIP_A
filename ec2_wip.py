import boto3

def client():
    return boto3.client('ec2')

def describe_instances():
    client = boto3.client('ec2')

response = client.describe_instances(
    InstanceIds=[
        'string'
    ],
    DryRun=True|False,
    Filters=[
        {
            'Name': 'string',
            'Values': [
                'string',
            ]
        },
    ]   
)
NextToken='string',
MaxResults=123