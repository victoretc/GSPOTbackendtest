import allure

from constants import tester_auth
from source.base.client import Requests
from source.enums.games import Utils


@allure.step('Get filters platforms list')
def get_filters_platforms_list(limit: int = None, offset: int = None, auth=tester_auth):
    params = {
        'limit': limit,
        'offset': offset
    }
    response = Requests.get(url=Utils.PLATFORMS, params=params, auth=auth)
    return response
