import time
from decimal import *

def amazon_webscraper():
    return {
        "ASIN": "test",
        "runtime": int(round(time.time() * 1000)),
        "itemName": "TestITEM",
        "price": Decimal(str('4.57878787'))
    }