import allure
import pytest

from source.api.languages import delete_languages
from source.base.validator import assert_status_code


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Test patch languages')
@pytest.mark.smoke
class TestLanguagesDelete:

    @allure.title('Test languages partial update')
    @allure.description('Проверка успешного ответа [204] при удалении языка')
    def test_languages_delete(self, create_test_languages):
        id_test = create_test_languages.json().get('id')
        response = delete_languages(id_data=id_test)
        assert_status_code(response=response, expected=204)
