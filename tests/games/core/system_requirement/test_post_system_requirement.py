import allure
import pytest

from source.api.games.system_requirement import create_system_requirement, delete_system_requirement
from source.base.generator import Generator
from source.schemas.games.system_requirement import SystemRequirement
from source.base.validator import assert_json_by_model, assert_status_code, assert_json_equal_json


@allure.epic('Games')
@allure.feature('Core')
@allure.story('System requirement')
@allure.suite('Test post system requirement')
@pytest.mark.smoke
class TestSystemRequirementCreate:
    @allure.title('Test system requirement create')
    @allure.description('Проверка успешного ответа [201] при создании системных требований')
    def test_system_requirement_create(self, delete_created_data):
        payload = Generator.object(model=SystemRequirement, seed=10)
        response = create_system_requirement(json=payload)

        payload['id'] = response.json().get('id')
        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=SystemRequirement)
        assert_json_equal_json(response=response, json=payload)

        id_data = response.json().get('id')
        delete_system_requirement(id_data=id_data)
