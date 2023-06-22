import allure

from source.api.genre import get_genre_list
from source.schemas.genre_schema import Genre
from source.base.validator import assert_status_code, assert_json_by_model


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Genre')
class TestGetGenre:

    @allure.title('Test genre list')
    @allure.description('Проверка успешного ответа [200] при запросе списка жанров')
    def test_get_genre_list(self):
        response = get_genre_list()
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Genre)
