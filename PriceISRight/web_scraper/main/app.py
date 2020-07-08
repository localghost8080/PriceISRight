from typing import Tuple

import boto3

from factory.EShopFactory import geteshop
from model.AmazonEShop import AmazonEShop
from factory import EShopFactory
from model.EShopName import EShopName

eshop = None
DYNAMODB = 'dynamodb'


def dynamoDBInsert(data: dict):
    dynamodb = boto3.resource(DYNAMODB)
    table = dynamodb.Table('PriceISRight')
    try:
        table.put_item(Item=data)
    except Exception as e:
        print("Exception happened" + str(e))


def lambda_handler(event, context):
    # TODO implement
    #print(event)
    item = derive_item_from_context(context)
    data = eshop.fetchprice(item)
    dynamoDBInsert(data)

    return {
        'statusCode': 200,
        'body': data
    }


def derive_item_from_context(context) -> Tuple[str, str]:
    global eshop
    eshop = geteshop(EShopName.AMAZON)
    return 'B07WHTTZW4' , 'https://www.amazon.in/TUF-Space-Grade-Resistance-Auto-Extreme-Compatibility/dp/B07WHTTZW4/ref=sr_1_1?dchild=1&keywords=B07WHTTZW4&qid=1594230816&sr=8-1'
