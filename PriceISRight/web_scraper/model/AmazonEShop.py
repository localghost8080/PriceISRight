import time
from decimal import Decimal
from typing import Tuple

from model.EShop import EShop
from model.EShopName import EShopName


class AmazonEShop(EShop):

    def __init__(self):
        EShop.__init__(self, EShopName.AMAZON)

    def __scrapingalgo(self, item: Tuple[str, str]):
        return {
            "ASIN": item[0],
            "runtime": int(round(time.time() * 1000)),
            "itemName": "TestITEM",
            "price": Decimal(str('4.57878787'))
        }

    def fetchprice(self, item: Tuple[str, str]):
        return self.__scrapingalgo(item)
