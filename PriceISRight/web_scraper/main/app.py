import boto3
from web_scraper import amazonwebscraper


def dynamoDBInsert(data):
    if (not isinstance(data, dict)):
        raise ValueError("is null or not a dictionary")
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('PriceISRight')
    try:
        table.put_item(Item=data)
    except Exception as e:
        print("Exception happened" + str(e))


def lambda_handler(event, context):
    # TODO implement
    print(event)
    data = amazonwebscraper.amazon_webscraper()
    dynamoDBInsert(data)

    return {
        'statusCode': 200,
        'body': data
    }