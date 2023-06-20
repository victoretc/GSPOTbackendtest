import pytest

from source.api.languages import create_languages, delete_languages
from source.base.generator import Generator
from source.schemas.laguage_schema import Language
from source.base.validator import assert_status_code


@pytest.fixture()
def test_data_languages():
    payload = Generator.object(model=Language, exclude="id")
    response = create_languages(json=payload)
    assert_status_code(response=response, expected=201)
    id_data = response.json().get('id')
    yield response
    response = delete_languages(id_data=id_data)
    assert_status_code(response=response, expected=204)

