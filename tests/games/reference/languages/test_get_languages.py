import allure
import pytest

from source.api.languages import get_languages_list
from source.base.validator import ResponseValidator
from source.schemas.laguage_schema import Language


@pytest.mark.regression
@allure.story('Проверка успешного ответа [200] при запросе списка языков.')
def test_get_languages_list():
    response = get_languages_list()
    result = ResponseValidator(response)
    result.assert_status_code(200)
    result.validate(Language)
    print(result.json_response)
