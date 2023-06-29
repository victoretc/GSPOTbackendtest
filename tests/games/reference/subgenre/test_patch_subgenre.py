import allure
import pytest


from source.schemas.subgenre import Subgenre
from source.base.generator import Generator
from source.api.subgenre import update_subgenre_partly
from source.base.validator import (assert_status_code, assert_json_equal_json,
                                   assert_json_by_model, assert_json_key_value)


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Subgenre')
@allure.suite('Test patch subgenre')
@pytest.mark.smoke
class TestSubgenrePartialUpdate:

    @allure.title('Test subgenre partial update')
    @allure.description('Проверка успешного ответа [200] при частичном обновлении поджанра')
    def test_subgenre_partial_update(self, create_delete_test_subgenre):
        id_test = create_delete_test_subgenre.json().get('id')

        payload = Generator.object(model=Subgenre)
        response = update_subgenre_partly(id_data=id_test, json=payload)
        payload['id'] = id_test

        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Subgenre)
        assert_json_equal_json(response=response, json=payload)
        assert_json_key_value(response=response, json=payload, key='name')
