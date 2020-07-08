from typing import Tuple

from model.EShopName import EShopName


class EShop:
    def __init__(self, platform: EShopName):
        self.platform = platform

    def fetchprice(self, item: Tuple[str, str]):
        raise NotImplementedError("This method is not implemented.")
