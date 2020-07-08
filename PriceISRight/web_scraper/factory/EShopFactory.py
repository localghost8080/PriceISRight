from model import EShop
from model.AmazonEShop import AmazonEShop
from model.EShopName import EShopName


def geteshop(shoptype: EShopName) -> EShop:
    if EShopName.AMAZON == shoptype:
        return AmazonEShop()
