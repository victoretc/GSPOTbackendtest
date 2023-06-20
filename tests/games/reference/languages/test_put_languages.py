import allure
import pytest

from source.base.generator import Generator
from source.api.languages import update_languages
from source.schemas.laguage_schema import Language
from source.base.validator import assert_json_by_model, assert_status_code, assert_json_key_value


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Test put languages')
@pytest.mark.smoke
class TestLanguagesUpdate:
    @allure.title("Test languages update")
    @allure.description('Проверка успешного ответа [200] при обновлении названия языка')
    def test_languages_update(self, test_data_languages):
        payload = Generator.object(model=Language, seed=2, exclude='id')
        id_data = test_data_languages.json().get('id')
        response = update_languages(id_data=id_data, json=payload)

        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Language)
        assert_json_key_value(response=response, payload=payload, key='name')
