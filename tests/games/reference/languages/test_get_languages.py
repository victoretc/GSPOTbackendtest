import allure
import pytest

from source.api.languages import get_languages_list
from source.schemas.laguage_schema import Language
from source.base.validator import assert_status_code, assert_json_by_model


@pytest.mark.regression
@allure.story('Проверка успешного ответа [200] при запросе списка языков.')
def test_get_languages_list():
    response = get_languages_list()
    assert_status_code(response=response, expected=200)
    assert_json_by_model(response=response, model=Language)

