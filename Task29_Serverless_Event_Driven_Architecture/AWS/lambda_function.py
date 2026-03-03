import boto3
import json
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('task5-table')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key    = record['s3']['object']['key']
        size   = record['s3']['object']['size']

        table.put_item(Item={
            'fileName': key,
            'bucketName': bucket,
            'fileSize': str(size),
            'uploadedAt': datetime.utcnow().isoformat()
        })
        print(f"Stored: {key} from {bucket}")

    return {'statusCode': 200, 'body': 'Success'}
