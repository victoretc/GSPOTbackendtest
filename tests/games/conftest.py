import pytest

from source.api.genre import create_genre, delete_genre
from source.api.languages import create_languages, delete_languages
from source.base.generator import Generator
from source.schemas.genre_schema import Genre
from source.schemas.laguage_schema import Language
from source.base.validator import assert_status_code


@pytest.fixture()
def create_delete_test_languages():
    payload = Generator.object(model=Language, exclude="id")
    response = create_languages(json=payload)
    assert_status_code(response=response, expected=201)
    id_test = response.json().get('id')
    yield response
    response = delete_languages(id_data=id_test)
    assert_status_code(response=response, expected=204)


@pytest.fixture()
def create_test_languages():
    payload = Generator.object(model=Language, exclude="id")
    response = create_languages(json=payload)
    assert_status_code(response=response, expected=201)
    return response


@pytest.fixture()
def create_delete_test_genre():
    payload = Generator.object(model=Genre, exclude="id")
    response = create_genre(json=payload)
    assert_status_code(response=response, expected=201)
    id_test = response.json().get('id')
    yield response
    response = delete_genre(id_data=id_test)
    assert_status_code(response=response, expected=204)


@pytest.fixture()
def create_test_genre():
    payload = Generator.object(model=Genre, exclude="id")
    response = create_genre(json=payload)
    assert_status_code(response=response, expected=201)
    return response
