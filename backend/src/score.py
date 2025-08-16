import os
import json
import boto3
import requests
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])
sns = boto3.client('sns')

SPORTS_API_URL = 'https://api.sportsdata.io/v3/scores/json/LiveScores' # Placeholder
API_KEY = 'YOUR_API_KEY' # Replace with your actual API key
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN', '')

def fetch_live_scores():
    headers = {'Ocp-Apim-Subscription-Key': API_KEY}
    response = requests.get(SPORTS_API_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    return []

def handler(event, context):
    method = event.get('httpMethod', 'GET')
    if method == 'GET':
        match_id = event.get('queryStringParameters', {}).get('MatchId')
        if match_id:
            resp = table.get_item(Key={'MatchId': match_id})
            return {'statusCode': 200, 'body': json.dumps(resp.get('Item', {}))}
        else:
            resp = table.scan()
            return {'statusCode': 200, 'body': json.dumps(resp.get('Items', []))}
    elif method == 'POST':
        body = json.loads(event['body'])
        table.put_item(Item=body)
        return {'statusCode': 201, 'body': json.dumps({'message': 'Score added'})}
    elif method == 'PUT':
        body = json.loads(event['body'])
        table.update_item(
            Key={'MatchId': body['MatchId']},
            UpdateExpression='SET #score = :score',
            ExpressionAttributeNames={'#score': 'Score'},
            ExpressionAttributeValues={':score': body['Score']}
        )
        return {'statusCode': 200, 'body': json.dumps({'message': 'Score updated'})}
    elif method == 'DELETE':
        match_id = event.get('queryStringParameters', {}).get('MatchId')
        if match_id:
            table.delete_item(Key={'MatchId': match_id})
            return {'statusCode': 200, 'body': json.dumps({'message': 'Score deleted'})}
        return {'statusCode': 400, 'body': json.dumps({'error': 'MatchId required'})}
    # Scheduled event: update scores
    elif event.get('source') == 'aws.events':
        scores = fetch_live_scores()
        for score in scores:
            table.put_item(Item=score)
            if SNS_TOPIC_ARN:
                sns.publish(TopicArn=SNS_TOPIC_ARN, Message=json.dumps(score))
        return {'statusCode': 200, 'body': json.dumps({'message': 'Scores updated'})}
    return {'statusCode': 405, 'body': json.dumps({'error': 'Method not allowed'})}
