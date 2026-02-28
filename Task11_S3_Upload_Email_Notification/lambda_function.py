import boto3
import json

def lambda_handler(event, context):
    sns = boto3.client('sns')
    
    # Extract S3 info from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    size = event['Records'][0]['s3']['object']['size']
    
    message = f"""New file uploaded to S3!

Bucket : {bucket}
File   : {key}
Size   : {size} bytes
"""
    
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:198116961487:s3-upload-alerts',
        Subject='S3 Upload Notification',
        Message=message
    )
    
    return {'statusCode': 200, 'body': 'Notification sent!'}

