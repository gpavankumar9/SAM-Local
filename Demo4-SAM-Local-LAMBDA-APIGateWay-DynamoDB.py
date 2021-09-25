import json
import boto3
import os

# import requests


def lambda_handler(event, context):
    #print(event)
    if os.getenv("AWS_SAM_LOCAL"):
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://dynamodb:8000")
    else:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ContactRequests')

    response =""
    if event['httpMethod'] == "POST":
        data = json.loads(event["body"])
        id = data['id']
        name = data['name']   
        response = table.put_item(
            Item={
                'id': id,
                'name': name,
                'email': "testEmail@gmail.com"
                }
            )

        response = "DynamoDB loaded with data"
    else:
        id = event['queryStringParameters']['id']
        name = event['queryStringParameters']['name']
        response = table.get_item(
            Key={
                'id': id,
                'name': name
            }
        )
        response = response['Item']        
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world test-lambda",
            "response": response
            # "location": ip.text.replace("\n", "")
        }),
    }
