import boto3
import json
# Demo lambda function meant for testing environment. 
# This fnc will operate on a Test table named DemoTable.
# Production Table will not get affected with tests and we can perform a full integration test.
dynamodb = boto3.resource('dynamodb')   
table = dynamodb.Table('MyDemoDynamodbTable') 

def lambda_handler(event, context):
    response = table.update_item(          
        Key = {                 
        "id" : 'id'
        },
        UpdateExpression = 'SET countvisits = countvisits + :val',  
        ExpressionAttributeValues={       
            ':val' : 1
        },
        ReturnValues="UPDATED_NEW"       
    )
    
    responseBody = json.dumps(int(response["Attributes"]["countvisits"])) 
    responseApi = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,x-requested-with',
            'Access-Control-Allow-Origin': '*', 
            'Access-Control-Allow-Methods': 'OPTIONS,GET'},
        'body': responseBody
    }
    return responseApi

