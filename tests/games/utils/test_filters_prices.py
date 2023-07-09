import allure
import pytest

from source.api.filters_prices import get_filters_prices_list
from source.schemas.min_max_price import MinMaxPrice
from source.base.validator import assert_status_code, assert_json_by_model


@allure.epic('Games')
@allure.feature('Utils')
@allure.story('Filters')
@allure.suite('Test get filters prices list')
@pytest.mark.smoke
class TestFiltersPrices:
    @allure.title('Test filters prices list')
    @allure.description('Проверка успешного ответа [200] при запросе списка фльтра цены')
    def test_filters_prices_list(self):
        response = get_filters_prices_list()
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=MinMaxPrice)
