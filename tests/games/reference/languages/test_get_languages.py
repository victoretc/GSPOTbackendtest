import allure
import pytest

from source.api.languages import get_languages, get_languages_list
from source.schemas.laguage_schema import Language
from source.base.validator import assert_status_code, assert_json_by_model


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Test get languages')
@pytest.mark.smoke
class TestGetLanguages:

    @allure.title('Test languages list')
    @allure.description('Проверка успешного ответа [200] при запросе списка языков.')
    def test_languages_list(self):
        response = get_languages_list()
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Language)

    @allure.title('Test languages read')
    @allure.description('Проверка успешного ответа [200] при запросе языка по ID.')
    def test_languages_read(self):
        response = get_languages(id_data=1)
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Language)
