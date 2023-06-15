import allure

from source.base.client import Requests
from constants import tester_auth
from source.enums.games import Reference


@allure.step('Get languages list')
def get_languages_list(limit: int = None, offset: int = None, auth=tester_auth):
    params = {
        'limit': limit,
        'offset': offset
    }
    response = Requests.get(url=Reference.LANGUAGES, params=params, auth=auth)
    return response


@allure.step('Create a language')
def create_languages(body, auth=tester_auth):
    response = Requests.post(url=Reference.LANGUAGES, json=body, auth=auth)
    return response

