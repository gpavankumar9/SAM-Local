import json
import os
import boto3
# import requests

s3_client = boto3.client("s3")

def lambda_handler(event, context):
    BUCKET = event['Records'][0]['s3']['bucket']['name']
    Key = event['Records'][0]['s3']['object']['key']
    result = s3_client.get_object(Bucket=BUCKET, Key=Key)
    #result = s3_client.get_object(Bucket='test-s3-pavan', Key='Input-file.json')
    data = json.loads(result["Body"].read().decode('utf-8-sig'))
    #print(data)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "Data":data
        }),
    }
