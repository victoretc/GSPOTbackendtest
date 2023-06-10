import allure
import requests

from requests.auth import HTTPBasicAuth
from source.base.validator import ResponseValidator
from source.schemas.laguage_schema import Language
from tests.games.constants import BASE_URL, LANGUAGES_URL


@allure.story('Проверка успешного ответа [201] при создании языка.')
def test_languages_create():
    url = BASE_URL + LANGUAGES_URL
    json_data = {
        'name': 'test_language'
    }
    response = requests.post(url=url, json=json_data, auth=HTTPBasicAuth(username="tester", password="tester"))
    result = ResponseValidator(response)
    result.assert_status_code(201)
    result.validate(Language)
    id_test = result.json_response.get("id")

    url_delete = BASE_URL + LANGUAGES_URL + str(id_test)
    response_delete = requests.delete(url=url_delete, auth=HTTPBasicAuth(username="tester", password="tester"))
    assert response_delete.status_code == 204
