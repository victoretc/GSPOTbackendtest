import allure
import pytest

from source.api.games.system_requirement import update_system_requirement_partly
from source.base.generator import Generator
from source.schemas.games.system_requirement import SystemRequirement
from source.base.validator import (assert_status_code, assert_json_by_model, assert_json_key_value)


@allure.epic('Games')
@allure.feature('Core')
@allure.story('System requirement')
@allure.suite('Test patch system requirement')
@pytest.mark.smoke
class TestSystemRequirementPartialUpdate:
    @allure.title('Test system requirement partial update')
    @allure.description('Проверка успешного ответа [200] при частичном обновлении системных требований')
    def test_system_requirement_partial_update(self):
        # id_test = create_delete_test_system_requirement.json().get('id')
        id_test = "9422a31d-f159-4bf4-98ce-90ee736a677f"
        payload = Generator.object(model=SystemRequirement, include='deviceGraphics')

        response = update_system_requirement_partly(id_data=id_test, json=payload)
        payload['id'] = id_test

        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=SystemRequirement)
        assert_json_key_value(response=response, json=payload, key='deviceGraphics')
