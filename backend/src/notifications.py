import boto3
import os
import json

sns = boto3.client('sns')
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN', '')

def send_notification(message):
    if SNS_TOPIC_ARN:
        sns.publish(TopicArn=SNS_TOPIC_ARN, Message=json.dumps(message))
        return True
    return False
