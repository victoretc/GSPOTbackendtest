import allure
import pytest

from source.api.product_languages import delete_product_languages
from source.base.validator import assert_status_code


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Product languages')
@allure.suite('Test delete product languages')
@pytest.mark.smoke
class TestProductLanguagesDelete:
    @allure.title('Test product languages delete')
    @allure.description('Проверка успешного ответа [204] при удалении языка продукта')
    def test_product_languages_delete(self, create_test_product_languages):
        id_test = create_test_product_languages.json().get('id')
        response = delete_product_languages(id_data=id_test)
        assert_status_code(response=response, expected=204)
