import boto3
import os

def get_cognito_client():
    return boto3.client('cognito-idp', region_name=os.environ.get('AWS_REGION', 'us-east-1'))

def create_user(username, password, email):
    client = get_cognito_client()
    user_pool_id = os.environ['COGNITO_USER_POOL_ID']
    response = client.admin_create_user(
        UserPoolId=user_pool_id,
        Username=username,
        UserAttributes=[
            {'Name': 'email', 'Value': email},
        ],
        TemporaryPassword=password,
        MessageAction='SUPPRESS'
    )
    return response

def authenticate_user(username, password):
    client = get_cognito_client()
    user_pool_id = os.environ['COGNITO_USER_POOL_ID']
    client_id = os.environ['COGNITO_CLIENT_ID']
    response = client.initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        },
        ClientId=client_id
    )
    return response
