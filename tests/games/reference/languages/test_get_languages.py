import allure
import pytest
import requests

from tests.games.constants import BASE_URL, LANGUAGES_LIST_URL
from source.base.validator import ResponseValidator
from source.schemas.laguage_schema import Language


@pytest.mark.regression
@allure.story('Проверка успешного ответа [200] при запросе списка языков.')
def test_get_languages_list():
    url = BASE_URL + LANGUAGES_LIST_URL
    with allure.step("GET REFERENCE LANGUAGES LIST"):
        response = requests.get(url=url)
        result = ResponseValidator(response)
    with allure.step("ASSERT STATUS CODE"):
        result.assert_status_code(200)
    with allure.step("VALIDATION JSON"):
        result.validate(Language)
