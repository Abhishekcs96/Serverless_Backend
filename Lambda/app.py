import boto3
import json

dynamodb = boto3.resource('dynamodb')   #resource dynamodb and set it as a variable to communicate with it
table = dynamodb.Table('MyDynamodbTable') #set table variable from the ddb resource table in aws.

def lambda_handler(event, context):
    response = table.update_item(          #Update the item in the table 
        Key = {                 #Specify the primary key of the item and then update the attribute of it(id is the primary key)
        "id" : 'id'
        },
        UpdateExpression = 'SET countvisits = countvisits + :val',  #We are able to access the countvisits field/attribute of this item and update it by adding a +val to it
        ExpressionAttributeValues={       # The value of the attribute that was used in the expression to update countvisits
            ':val' : 1
        },
        ReturnValues="UPDATED_NEW"        #return only the newly updated values. # return response - Returns a dictionary, we need to convert this to json
    )
    #Response is returned as a dict. We can access the keys of a dict by directly referencing it
    #Tried using keys() method but doesnt seem to be the way to access a key within a key(dict within a dict)
    responseBody = json.dumps(int(response["Attributes"]["countvisits"])) # json.dumps converts a python object(dict) into a js string. 
    responseApi = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'https://achandrasekar.com', 
            'Access-Control-Allow-Origin': 'http://achandrasekar.com',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'},
        'body': responseBody
    }
    return responseApi

