import allure
import requests

from tests.games.constants import BASE_URL, GET_REFERENCE_GENRE_LIST_URL
from source.base.validator import ResponseValidator
from source.schemas.genre_schema import Genre


@allure.story('Проверка успешного ответа [200] при запросе списка жанров.')
def test_get_reference_genre_list():
    url = BASE_URL + GET_REFERENCE_GENRE_LIST_URL
    with allure.step("GET REFERENCE GENRE LIST"):
        response = requests.get(url=url)
        result = ResponseValidator(response)
    with allure.step("ASSERT STATUS CODE"):
        result.assert_status_code(200)
    with allure.step("VALIDATION JSON"):
        result.validate(Genre)
