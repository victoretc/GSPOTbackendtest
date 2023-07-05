from enum import Enum


BASE_URL = "https://payments.alpha.g-spot.website/api/v1/"


class External_Payments(str, Enum):
    ACCEPT_PAYMENT = f'{BASE_URL}external_payments/accept_payment/'
    COMISSIONS = f'{BASE_URL}external_payments/comissions/'
    SERVICES = f'{BASE_URL}external_payments/services/'

    def __str__(self) -> str:
        return self.value


class Item_Purchases(str, Enum):
    ITEM_PURCHASE_HISTORY = f'{BASE_URL}item_purchases/item-purchase-history/'
    PURCHASE = f'{BASE_URL}item_purchases/purchase/'
    REFUND = f'{BASE_URL}item_purchases/refund/'

    def __str__(self) -> str:
        return self.value