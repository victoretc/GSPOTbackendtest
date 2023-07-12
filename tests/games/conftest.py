import pytest

from source.api.games.system_requirement import create_system_requirement, delete_system_requirement
from source.api.genre import create_genre, delete_genre
from source.api.languages import create_languages, delete_languages
from source.api.product_languages import create_product_languages, delete_product_languages
from source.api.subgenre import create_subgenre, delete_subgenre
from source.base.generator import Generator
from source.schemas.games.system_requirement import SystemRequirement
from source.schemas.genre_schema import Genre
from source.schemas.laguage_schema import Language
from source.base.validator import assert_status_code
from source.schemas.product_languages import ProductLanguages
from source.schemas.subgenre import Subgenre


@pytest.fixture()
def create_delete_test_languages():
    payload = Generator.object(model=Language)
    response = create_languages(json=payload)
    assert_status_code(response=response, expected=201)
    id_test = response.json().get('id')
    yield response
    response = delete_languages(id_data=id_test)
    assert_status_code(response=response, expected=204)


@pytest.fixture()
def create_test_languages():
    payload = Generator.object(model=Language)
    response = create_languages(json=payload)
    assert_status_code(response=response, expected=201)
    return response


@pytest.fixture()
def create_delete_test_product_languages():
    payload = Generator.object(model=ProductLanguages)
    response = create_product_languages(json=payload)
    assert_status_code(response=response, expected=201)
    id_test = response.json().get('id')
    yield response
    response = delete_product_languages(id_data=id_test)
    assert_status_code(response=response, expected=204)


@pytest.fixture()
def create_test_product_languages():
    payload = Generator.object(model=ProductLanguages)
    response = create_product_languages(json=payload)
    assert_status_code(response=response, expected=201)
    return response


@pytest.fixture()
def create_delete_test_genre():
    payload = Generator.object(model=Genre)
    response = create_genre(json=payload)
    assert_status_code(response=response, expected=201)
    id_test = response.json().get('id')
    yield response
    response = delete_genre(id_data=id_test)
    assert_status_code(response=response, expected=204)


@pytest.fixture()
def create_test_genre():
    payload = Generator.object(model=Genre)
    response = create_genre(json=payload)
    assert_status_code(response=response, expected=201)
    return response


@pytest.fixture()
def create_delete_test_subgenre():
    payload = Generator.object(model=Subgenre)
    response = create_subgenre(json=payload)
    assert_status_code(response=response, expected=201)
    id_test = response.json().get('id')
    yield response
    response = delete_subgenre(id_data=id_test)
    assert_status_code(response=response, expected=204)


@pytest.fixture()
def create_test_subgenre():
    payload = Generator.object(model=Subgenre)
    response = create_subgenre(json=payload)
    assert_status_code(response=response, expected=201)
    return response


@pytest.fixture()
def create_delete_test_system_requirement():
    payload = Generator.object(model=SystemRequirement)
    response = create_system_requirement(json=payload)
    assert_status_code(response=response, expected=201)
    id_test = response.json().get('id')
    yield response
    response = delete_system_requirement(id_data=id_test)
    assert_status_code(response=response, expected=204)


@pytest.fixture()
def create_test_system_requirement():
    payload = Generator.object(model=SystemRequirement)
    response = create_system_requirement(json=payload)
    assert_status_code(response=response, expected=201)
    return response
