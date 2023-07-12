import allure
import pytest

from source.base.generator import Generator
from source.enums.expected import ExpectedJSON
from source.schemas.laguage_schema import Language
from source.api.languages import create_languages, delete_languages
from source.base.validator import (assert_json_by_model, assert_json_key_value,
                                   assert_status_code, assert_json_equal_json)


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Test post languages')
@pytest.mark.smoke
class TestLanguagesCreate:
    @allure.title('Test languages create')
    @allure.description('Проверка успешного ответа [201] при создании языка.')
    def test_languages_create(self, delete_created_data):
        payload = Generator.object(model=Language, seed=1)
        response = create_languages(json=payload)

        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=Language)
        assert_json_key_value(response=response, json=payload, key='name')

        id_data = response.json().get("id")
        delete_created_data(api=delete_languages, id_data=id_data)


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Regression-tests post languages')
@pytest.mark.regression
class TestLanguagesCreateRegression:
    @allure.title('Test languages create with checking the boundary values')
    @allure.description('Проверка граничных значений поля "name" при создании языка')
    @pytest.mark.parametrize("value, expected, massage", [
        ("", 400, ExpectedJSON.FIELD_CANNOT_BE_EMPTY.value),
        ("e", 201, None),
        ("qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop", 201,
         None),
        ("qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopA", 400,
         ExpectedJSON.FIELD_CANNOT_CONTAINS_MORE_100.value)
    ])
    def test_languages_create_with_boundary_values(self, value, expected, massage, delete_created_data):
        payload = Generator.object(model=Language, name=value)
        response = create_languages(json=payload)
        if len(value) < 1 or len(value) > 100:
            expected_json = ExpectedJSON.key_value(key='name', value=massage)
            assert_status_code(response=response, expected=expected)
            assert_json_equal_json(response=response, json=expected_json)
        else:
            assert_status_code(response=response, expected=expected)
            assert_json_by_model(response=response, model=Language)
            assert_json_key_value(response=response, json=payload, key='name')

            id_data = response.json().get("id")
            delete_created_data(api=delete_languages, id_data=id_data)

    @allure.title('Test languages create with invalid name')
    @allure.description('Проверка ответа [400] при создании языка c невалидным значением')
    @pytest.mark.parametrize("value", [
        "   ", 1234567890, u"下来顔文字", u"Հայկականتحتاجفقطإلىنسخלבדוק", "Ru En", "~!@#$%^&*()_+<>?:/|{}[]';,.`-="
    ])
    def test_languages_create_with_invalid_name(self, value, delete_created_data):
        payload = Generator.object(model=Language, name=value)
        response = create_languages(json=payload)

        if response.status_code == 201:
            id_data = response.json().get("id")
            delete_created_data(api=delete_languages, id_data=id_data)

        expected = ExpectedJSON.key_value(key='name', value=ExpectedJSON.FIELD_CANNOT_BE_EMPTY.value)
        assert_status_code(response=response, expected=400)
        assert_json_equal_json(response=response, json=expected)

    @allure.title('Test languages create with atypical value')
    @allure.description('Проверка ответа [200] при создании нетипичного значения языка')
    @pytest.mark.parametrize("value", [
        " ru", "ru ", "EnGlIsH"
    ])
    def test_languages_create_with_atypical_value(self, value, delete_created_data):
        payload = Generator.object(model=Language, name=value)
        response = create_languages(json=payload)

        payload['name'] = value.strip()
        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=Language)
        assert_json_key_value(response=response, json=payload, key='name')

        id_data = response.json().get("id")
        delete_created_data(api=delete_languages, id_data=id_data)
