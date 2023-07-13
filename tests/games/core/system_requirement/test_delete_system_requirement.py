import allure
import pytest

from source.api.games.system_requirement import delete_system_requirement
from source.base.validator import assert_status_code


@allure.epic('Games')
@allure.feature('Core')
@allure.story('System requirement')
@allure.suite('Test delete system requirement')
@pytest.mark.smoke
class TestSystemRequirementDelete:
    @allure.title('Test system requirement delete')
    @allure.description('Проверка успешного ответа [204] при удалении системных требований')
    def test_system_requirement_delete(self, create_test_system_requirement):
        id_test = create_test_system_requirement.json().get('id')
        response = delete_system_requirement(id_data=id_test)
        assert_status_code(response=response, expected=204)
