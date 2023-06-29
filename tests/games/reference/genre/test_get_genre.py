import allure
import pytest

from source.schemas.genre_schema import Genre
from source.api.genre import get_genre_list, get_genre
from source.base.validator import assert_status_code, assert_json_by_model, assert_json_key_value


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Genre')
@allure.suite('Test get genre')
@pytest.mark.smoke
class TestGenre:

    @allure.title('Test genre list')
    @allure.description('Проверка успешного ответа [200] при запросе списка жанров')
    def test_genre_list(self):
        response = get_genre_list()
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Genre)

    @allure.title('Test genre read')
    @allure.description('Проверка успешного ответа [200] при запросе жанра по ID.')
    def test_genre_read(self, create_delete_test_genre):
        id_test = create_delete_test_genre.json().get('id')
        response = get_genre(id_data=id_test)
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Genre)
        assert_json_key_value(response=response, json=create_delete_test_genre.json(), key='id')
