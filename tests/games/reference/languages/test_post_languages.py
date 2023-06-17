import allure
from source.base.validator import ResponseValidator
from source.schemas.laguage_schema import Language
from source.api.languages import create_languages, delete_languages


@allure.story('Проверка успешного ответа [201] при создании языка.')
def test_languages_create(delete_created_data):
    payload = Language.random().dict(exclude_none=True)
    response = create_languages(json=payload)
    result = ResponseValidator(response)
    result.assert_status_code(201)
    result.validate(Language)
    id_data = result.json_response.get("id")

    delete_created_data(api=delete_languages, id_data=id_data)
