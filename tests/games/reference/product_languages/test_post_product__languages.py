import allure
import pytest

from source.base.generator import Generator
from source.schemas.product_languages import ProductLanguages
from source.api.product_languages import delete_product_languages, create_product_languages
from source.base.validator import assert_json_by_model, assert_json_key_value, assert_status_code


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Product languages')
@allure.suite('Test post product languages')
@pytest.mark.smoke
class TestProductLanguagesCreate:
    @allure.title('Test product languages create')
    @allure.description('Проверка успешного ответа [201] при создании языка продукта.')
    def test_product_languages_create(self, delete_created_data):
        payload = Generator.object(model=ProductLanguages, seed=111)
        response = create_product_languages(json=payload)

        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=ProductLanguages)
        assert_json_key_value(response=response, json=payload, key='name')

        id_data = response.json().get("id")
        delete_created_data(api=delete_product_languages, id_data=id_data)
