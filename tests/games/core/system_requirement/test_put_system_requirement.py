import allure
import pytest

from source.api.games.system_requirement import update_system_requirement
from source.base.generator import Generator
from source.schemas.games.system_requirement import SystemRequirement
from source.base.validator import (assert_status_code, assert_json_by_model, assert_json_equal_json)


@allure.epic('Games')
@allure.feature('Core')
@allure.story('System requirement')
@allure.suite('Test put system requirement')
@pytest.mark.smoke
class TestSystemRequirementUpdate:
    @allure.title('Test system requirement update')
    @allure.description('Проверка успешного ответа [201] при обновлении системных требований')
    def test_system_requirement_update(self, create_delete_test_system_requirement):
        id_test = create_delete_test_system_requirement.json().get('id')

        payload = Generator.object(model=SystemRequirement)
        response = update_system_requirement(id_data=id_test, json=payload)
        payload['id'] = id_test

        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=SystemRequirement)
        assert_json_equal_json(response=response, json=payload)
