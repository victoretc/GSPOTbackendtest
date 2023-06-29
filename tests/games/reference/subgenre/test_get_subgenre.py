import allure
import pytest


from source.schemas.subgenre import Subgenre
from source.api.subgenre import get_subgenre_list, get_subgenre
from source.base.validator import assert_status_code, assert_json_by_model, assert_json_key_value


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Subgenre')
@allure.suite('Test get subgenre')
@pytest.mark.smoke
class TestSubgenre:
    @allure.title('Test subgenre list')
    @allure.description('Проверка успешного ответа [200] при запросе списка поджанров')
    def test_subgenre_list(self):
        response = get_subgenre_list()
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Subgenre)

    @allure.title('Test subgenre read')
    @allure.description('Проверка успешного ответа [200] при запросе поджанра по ID.')
    def test_genre_read(self, create_delete_test_subgenre):
        id_test = create_delete_test_subgenre.json().get('id')
        response = get_subgenre(id_data=id_test)
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Subgenre)
        assert_json_key_value(response=response, json=create_delete_test_subgenre.json(), key='id')
