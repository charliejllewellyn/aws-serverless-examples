import boto3

def lambda_handler(event, context):
    # TODO implement
    ec2 = boto3.client('ec2')
    ec2response = ec2.describe_instances()
    
    snsclient = boto3.client('sns')
    response = snsclient.publish(
    TopicArn='arn:aws:sns:us-east-1:307399572026:ec2Topic',
    Message=str(ec2response),
    Subject='ec2 rep'
    )
    
    return 'Hello from Lambda'
