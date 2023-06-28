import allure
import pytest

from source.base.generator import Generator
from source.schemas.subgenre import Subgenre
from source.api.subgenre import delete_subgenre, create_subgenre
from source.base.validator import assert_json_by_model, assert_json_key_value, assert_status_code


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Subgenre')
@allure.suite('Test post Subgenre')
@pytest.mark.smoke
class TestGenreCreate:

    @allure.title('Test subgenre create')
    @allure.description('Проверка успешного ответа [201] при создании поджанра')
    def test_subgenre_create(self, delete_created_data):
        payload = Generator.object(model=Subgenre)
        response = create_subgenre(json=payload)

        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=Subgenre)
        assert_json_key_value(response=response, json=payload, key='name')

        id_data = response.json().get('id')
        delete_created_data(api=delete_subgenre, id_data=id_data)
