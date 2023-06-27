import allure
import pytest

from source.api.genre import update_genre_partly
from source.base.generator import Generator
from source.schemas.genre_schema import Genre
from source.base.validator import (assert_status_code, assert_json_equal_json,
                                   assert_json_by_model, assert_json_key_value)


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Genre')
@allure.suite('Test patch genre')
@pytest.mark.smoke
class TestGenrePartialUpdate:

    @allure.title('Test genre partial update')
    @allure.description('Проверка успешного ответа [200] при частичном обновлении жанра')
    def test_genre_partial_update(self, create_delete_test_genre):
        id_test = create_delete_test_genre.json().get('id')

        payload = Generator.object(model=Genre)
        response = update_genre_partly(id_data=id_test, json=payload)
        payload['id'] = id_test

        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Genre)
        assert_json_equal_json(response=response, json=payload)
        assert_json_key_value(response=response, json=payload, key='name')
