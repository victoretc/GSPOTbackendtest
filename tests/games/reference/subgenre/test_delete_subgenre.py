import allure
import pytest


from source.api.subgenre import delete_subgenre
from source.base.validator import assert_status_code


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Subgenre')
@allure.suite('Test delete subgenre')
@pytest.mark.smoke
class TestSubgenreDelete:
    @allure.title('Test subgenre delete')
    @allure.description('Проверка успешного ответа [204] при удалении поджанра')
    def test_subgenre_delete(self, create_test_subgenre):
        id_test = create_test_subgenre.json().get('id')
        response = delete_subgenre(id_data=id_test)
        assert_status_code(response=response, expected=204)
