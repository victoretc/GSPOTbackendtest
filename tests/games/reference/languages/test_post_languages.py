import allure
import requests

from requests.auth import HTTPBasicAuth
from source.base.validator import ResponseValidator
from source.schemas.laguage_schema import CreateLanguage, Language
from tests.games.constants import BASE_URL, LANGUAGES_URL


@allure.story('Проверка успешного ответа [201] при создании языка.')
def test_languages_create(delete_created_data):
    url = BASE_URL + LANGUAGES_URL
    json_data = CreateLanguage().dict()
    response = requests.post(url=url, json=json_data, auth=HTTPBasicAuth(username="tester", password="tester"))
    result = ResponseValidator(response)
    result.assert_status_code(201)
    result.validate(Language)
    test_id = result.json_response.get("id")

    delete_created_data(BASE_URL, LANGUAGES_URL, test_id)
