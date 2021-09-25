import json
import os
import boto3
# import requests

def lambda_handler(event, context):

    data = json.loads(event["body"])
    message = data['message']
    id = data['id']
    name = data['name']
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            "id":id,
            "name":name,
        }),
    }
