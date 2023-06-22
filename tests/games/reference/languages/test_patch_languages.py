import allure
import pytest

from source.base.generator import Generator
from source.api.languages import update_languages_partly
from source.schemas.laguage_schema import Language
from source.base.validator import (assert_json_by_model, assert_status_code,
                                   assert_json_key_value, assert_json_equal_json)


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Test patch languages')
@pytest.mark.smoke
class TestLanguagesPartialUpdate:

    @allure.title('Test languages partial update')
    @allure.description('Проверка успешного ответа [200] при частичном обновлении языка')
    def test_languages_partial_update(self, create_delete_test_languages):
        id_test = create_delete_test_languages.json().get('id')

        payload = Generator.object(model=Language, seed=2, include='name')
        response = update_languages_partly(id_data=id_test, json=payload)
        payload['id'] = id_test

        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Language)
        assert_json_equal_json(response=response, json=payload)
        assert_json_key_value(response=response, json=payload, key='name')
