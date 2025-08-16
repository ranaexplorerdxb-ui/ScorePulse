import os
import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

# Store favorite teams for premium users

def handler(event, context):
    method = event.get('httpMethod', 'GET')
    user_id = event.get('requestContext', {}).get('authorizer', {}).get('claims', {}).get('sub')
    if not user_id:
        return {'statusCode': 401, 'body': json.dumps({'error': 'Unauthorized'})}
    if method == 'GET':
        resp = table.get_item(Key={'MatchId': f'FAVORITES#{user_id}'})
        return {'statusCode': 200, 'body': json.dumps(resp.get('Item', {}))}
    elif method == 'POST':
        body = json.loads(event['body'])
        table.put_item(Item={'MatchId': f'FAVORITES#{user_id}', 'Favorites': body['Favorites']})
        return {'statusCode': 201, 'body': json.dumps({'message': 'Favorites updated'})}
    return {'statusCode': 405, 'body': json.dumps({'error': 'Method not allowed'})}
