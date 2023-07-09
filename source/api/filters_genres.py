import allure

from constants import tester_auth
from source.base.client import Requests
from source.enums.games import Utils


@allure.step('Get filters genres list')
def get_filters_genres_list(limit: int = None, offset: int = None, auth=tester_auth):
    params = {
        'limit': limit,
        'offset': offset
    }
    response = Requests.get(url=Utils.GENRES, params=params, auth=auth)
    return response

