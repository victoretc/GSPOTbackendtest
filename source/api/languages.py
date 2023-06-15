import allure

from source.base.client import Requests
from constants import tester_auth
from tests.games.constants import BASE_URL, LANGUAGES_URL, LANGUAGES_LIST_URL


@allure.step('Get languages list')
def get_languages_list(auth=tester_auth):
    url = BASE_URL + LANGUAGES_LIST_URL
    response = Requests.get(url=url, auth=auth)
    return response


@allure.step('Create a language')
def create_language(body, auth=tester_auth):
    url = BASE_URL + LANGUAGES_URL
    response = Requests.post(url=url, json=body, auth=auth)
    return response
