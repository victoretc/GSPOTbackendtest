import allure

from constants import tester_auth
from source.base.client import Requests
from source.enums.games import Reference


@allure.step('Get subgenre by id {id_data}')
def get_subgenre(id_data: int, auth=tester_auth):
    url = f'{Reference.SUBGENRE}{id_data}'
    response = Requests.get(url=url, auth=auth)
    return response


@allure.step('Get subgenres list')
def get_subgenre_list(limit: int = None, offset: int = None, auth=tester_auth):
    params = {
        'limit': limit,
        'offset': offset
    }
    response = Requests.get(url=Reference.SUBGENRE, params=params, auth=auth)
    return response


@allure.step('Create a subgenre')
def create_subgenre(json, auth=tester_auth):
    response = Requests.post(url=Reference.SUBGENRE, json=json, auth=auth)
    return response


@allure.step('Update the subgenre with id "{id_data}"')
def update_subgenre(id_data: int, json, auth=tester_auth):
    url = f'{Reference.SUBGENRE}{id_data}/'
    response = Requests.put(url=url, json=json, auth=auth)
    return response


@allure.step('Update the subgenre partly with id "{id_data}"')
def update_subgenre_partly(id_data: int, json, auth=tester_auth):
    url = f'{Reference.SUBGENRE}{id_data}/'
    response = Requests.patch(url=url, json=json, auth=auth)
    return response


@allure.step('Delete the subgenre with id "{id_data}"')
def delete_subgenre(id_data: int, auth=tester_auth):
    url = f'{Reference.SUBGENRE}{id_data}'
    response = Requests.delete(url=url, auth=auth)
    return response
