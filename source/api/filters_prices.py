import allure

from constants import tester_auth
from source.base.client import Requests
from source.enums.games import Utils


@allure.step('Get filters prices list')
def get_filters_prices_list(limit: int = None, offset: int = None, auth=tester_auth):
    params = {
        'limit': limit,
        'offset': offset
    }
    response = Requests.get(url=Utils.PRICES, params=params, auth=auth)
    return response
