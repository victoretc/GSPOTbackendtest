import allure
import pytest

from source.schemas.genre_games import GenreGames
from source.api.filters_genres import get_filters_genres_list
from source.base.validator import assert_status_code, assert_json_by_model


@allure.epic('Games')
@allure.feature('Utils')
@allure.story('Genres')
@allure.suite('Test get filters genres list')
@pytest.mark.smoke
class TestFiltersGenres:
    @allure.title('Test filters genres list')
    @allure.description('Проверка успешного ответа [200] при запросе фильтра по жанру игр')
    def test_filters_genres_list(self):
        response = get_filters_genres_list()
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=GenreGames)
