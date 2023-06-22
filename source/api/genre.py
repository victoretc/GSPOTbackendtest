import allure

from constants import tester_auth
from source.base.client import Requests
from source.enums.games import Reference


@allure.step('Get genre by id {id_data}')
def get_genre(id_data: int, auth=tester_auth):
    url = f'{Reference.GENRE}{id_data}'
    response = Requests.get(url=url, auth=auth)
    return response


@allure.step('Get genres list')
def get_genre_list(limit: int = None, offset: int = None, auth=tester_auth):
    params = {
        'limit': limit,
        'offset': offset
    }
    response = Requests.get(url=Reference.GENRE, params=params, auth=auth)
    return response


@allure.step('Create a genre')
def create_genre(json, auth=tester_auth):
    response = Requests.post(url=Reference.GENRE, json=json, auth=auth)
    return response


@allure.step('Update the genre with id "{id_data}"')
def update_genre(id_data: int, json, auth=tester_auth):
    url = f'{Reference.GENRE}{id_data}/'
    response = Requests.put(url=url, json=json, auth=auth)
    return response


@allure.step('Update the genre partly with id "{id_data}"')
def update_genre_partly(id_data: int, json, auth=tester_auth):
    url = f'{Reference.GENRE}{id_data}/'
    response = Requests.patch(url=url, json=json, auth=auth)
    return response


@allure.step('Delete the genre with id "{id_data}"')
def delete_genre(id_data: int, auth=tester_auth):
    url = f'{Reference.GENRE}{id_data}'
    response = Requests.delete(url=url, auth=auth)
    return response
