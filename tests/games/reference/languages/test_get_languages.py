import allure
import pytest

from source.api.languages import get_languages, get_languages_list, delete_languages
from source.enums.expected import ExpectedJSON
from source.schemas.laguage_schema import Language
from source.base.validator import (assert_status_code, assert_json_by_model,
                                   assert_json_key_value, assert_json_equal_json)


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Test get languages')
@pytest.mark.smoke
class TestLanguages:
    @allure.title('Test languages list')
    @allure.description('Проверка успешного ответа [200] при запросе списка языков.')
    def test_languages_list(self):
        response = get_languages_list()
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Language)

    @allure.title('Test languages read')
    @allure.description('Проверка успешного ответа [200] при запросе языка по ID.')
    def test_languages_read(self, create_delete_test_languages):
        id_test = create_delete_test_languages.json().get('id')
        response = get_languages(id_data=id_test)
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Language)
        assert_json_key_value(response=response, json=create_delete_test_languages.json(), key='id')


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Regression-tests get languages')
@pytest.mark.regression
class TestLanguagesRegression:
    @allure.title('Test read a language with a non-existent ID')
    @allure.description('Проверка ответа [404] при запросе языка c несуществующим ID')
    def test_language_read_with_non_existent_id(self):
        response = get_languages(id_data=-1)
        assert_status_code(response=response, expected=404)
        assert_json_equal_json(response=response, json=ExpectedJSON.NOT_FOUND.value)

    @allure.title('Test read a language with a deleted ID')
    @allure.description('Проверка ответа [404] при запросе удаленного языка')
    def test_language_read_with_deleted_id(self, create_test_languages, delete_created_data):
        id_test = create_test_languages.json().get('id')
        delete_created_data(api=delete_languages, id_data=id_test)

        response = get_languages(id_data=id_test)
        assert_status_code(response=response, expected=404)
        assert_json_equal_json(response=response, json=ExpectedJSON.NOT_FOUND.value)
