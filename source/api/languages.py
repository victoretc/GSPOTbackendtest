import allure

from constants import tester_auth
from source.base.client import Requests
from source.enums.games import Reference


@allure.step('Get languages with id "{languages_id}"')
def get_languages(languages_id: int, auth=tester_auth):
    url = f'{Reference.LANGUAGES}{languages_id}'
    response = Requests.get(url=url, auth=auth)
    return response


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


@allure.step('Update the language')
def update_languages(languages_id: int, body, auth=tester_auth):
    url = f'{Reference.LANGUAGES}{languages_id}'
    response = Requests.put(url=url, json=body, auth=auth)
    return response


@allure.step('Update the language partly')
def update_languages_partly(languages_id: int, body, auth=tester_auth):
    url = f'{Reference.LANGUAGES}{languages_id}'
    response = Requests.patch(url=url, json=body, auth=auth)
    return response


@allure.step('Delete the language')
def delete_languages(languages_id: int, auth=tester_auth):
    url = f'{Reference.LANGUAGES}{languages_id}'
    response = Requests.delete(url=url, auth=auth)
    return response
