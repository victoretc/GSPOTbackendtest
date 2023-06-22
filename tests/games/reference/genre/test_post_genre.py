import allure
import pytest

from source.api.genre import create_genre, delete_genre
from source.base.generator import Generator
from source.base.validator import assert_json_by_model, assert_json_key_value, assert_status_code
from source.schemas.genre_schema import Genre


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Test post genre')
@pytest.mark.smoke
class TestGenreCreate:

    @allure.title('Test genre create')
    @allure.description('Проверка успешного ответа [201] при создании жанра')
    def test_genre_create(self, delete_created_data):
        payload = Generator.object(model=Genre, exclude='id')
        response = create_genre(json=payload)

        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=Genre)
        assert_json_key_value(response=response, json=payload, key='name')

        id_data = response.json().get('id')
        delete_created_data(api=delete_genre, id_data=id_data)
