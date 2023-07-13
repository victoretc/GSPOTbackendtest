import allure

from constants import tester_auth
from source.base.client import Requests
from source.enums.games import Core


@allure.step('Get the system requirement by id "{id_data}"')
def get_system_requirement(id_data: str, auth=tester_auth):
    url = f'{Core.SYSTEM_REQUIREMENT}{id_data}'
    response = Requests.get(url=url, auth=auth)
    return response


@allure.step('Get system requirement list')
def get_system_requirement_list(limit: int = None, offset: int = None, auth=tester_auth):
    params = {
        'limit': limit,
        'offset': offset
    }
    response = Requests.get(url=Core.SYSTEM_REQUIREMENT, params=params, auth=auth)
    return response


@allure.step('Create a system requirement')
def create_system_requirement(json, auth=tester_auth):
    response = Requests.post(url=Core.SYSTEM_REQUIREMENT, json=json, auth=auth)
    return response


@allure.step('Update the system requirement with id "{id_data}"')
def update_system_requirement(id_data: str, json, auth=tester_auth):
    url = f'{Core.SYSTEM_REQUIREMENT}{id_data}/'
    response = Requests.put(url=url, json=json, auth=auth)
    return response


@allure.step('Update the system requirement partly with id "{id_data}"')
def update_system_requirement_partly(id_data: str, json, auth=tester_auth):
    url = f'{Core.SYSTEM_REQUIREMENT}{id_data}/'
    response = Requests.patch(url=url, json=json, auth=auth)
    return response


@allure.step('Delete the system requirement with id "{id_data}"')
def delete_system_requirement(id_data: str, auth=tester_auth):
    url = f'{Core.SYSTEM_REQUIREMENT}{id_data}'
    response = Requests.delete(url=url, auth=auth)
    return response
