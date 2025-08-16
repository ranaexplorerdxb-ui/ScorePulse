# ScorePulse Backend Infrastructure

This folder contains the AWS SAM template for deploying the ScorePulse backend services:
- DynamoDB table for scores
- Lambda function for score updates and API
- API Gateway for REST endpoints
- Cognito User Pool for authentication
- SNS Topic for live score notifications
- S3 bucket for static assets
- CloudFront distribution for global access

## Deployment

1. Install AWS SAM CLI: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html
2. Build and deploy:
   ```
   sam build
   sam deploy --guided
   ```
3. Update frontend `aws-exports.js` with deployed resource values.
