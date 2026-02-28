import urllib.request
import boto3
import os

WEBSITE_URL = "https://google.com"   # change to your target URL
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:198116961487:website-down-alerts"

def lambda_handler(event, context):
    sns = boto3.client('sns')

    try:
        response = urllib.request.urlopen(WEBSITE_URL, timeout=10)
        status = response.getcode()

        if status == 200:
            print(f"Website UP: {WEBSITE_URL} - Status {status}")
            return {'statusCode': 200, 'body': 'Website is UP'}
        else:
            raise Exception(f"Unexpected status code: {status}")

    except Exception as e:
        message = f"""ALERT: Website Down!

URL    : {WEBSITE_URL}
Error  : {str(e)}
Action : Please investigate immediately.
"""
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject='ALERT: Website Down!',
            Message=message
        )
        print(f"Alert sent! Error: {e}")
        return {'statusCode': 500, 'body': 'Website is DOWN - Alert sent'}
