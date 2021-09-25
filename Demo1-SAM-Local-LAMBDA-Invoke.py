import json
# import requests


def lambda_handler(event, context):
    
    data = "Invoke LAMBDA in Local"
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "Data":data
        }),
    }
