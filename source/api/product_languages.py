import allure

from constants import tester_auth
from source.base.client import Requests
from source.enums.games import Reference


@allure.step('Get the product language by id {id_data}')
def get_product_languages(id_data: int, auth=tester_auth):
    url = f'{Reference.PRODUCT_LANGUAGES}{id_data}'
    response = Requests.get(url=url, auth=auth)
    return response


@allure.step('Get product languages list')
def get_product_languages_list(limit: int = None, offset: int = None, auth=tester_auth):
    params = {
        'limit': limit,
        'offset': offset
    }
    response = Requests.get(url=Reference.PRODUCT_LANGUAGES, params=params, auth=auth)
    return response


@allure.step('Create a product language')
def create_product_languages(json, auth=tester_auth):
    response = Requests.post(url=Reference.PRODUCT_LANGUAGES, json=json, auth=auth)
    return response


@allure.step('Update the product language with id "id_data"')
def update_product_languages(id_data: int, json, auth=tester_auth):
    url = f'{Reference.PRODUCT_LANGUAGES}{id_data}/'
    response = Requests.put(url=url, json=json, auth=auth)
    return response


@allure.step('Update the product language partly with id "{id_data}"')
def update_product_languages_partly(id_data: int, json, auth=tester_auth):
    url = f'{Reference.PRODUCT_LANGUAGES}{id_data}/'
    response = Requests.patch(url=url, json=json, auth=auth)
    return response


@allure.step('Delete the poduct language with id "id_data"')
def delete_product_languages(id_data: int, auth=tester_auth):
    url = f'{Reference.PRODUCT_LANGUAGES}{id_data}'
    response = Requests.delete(url=url, auth=auth)
    return response
