import pytest


def _delete_created_data(api, id_data):
    response_delete = api(id_data=id_data)
    assert response_delete.status_code == 204


@pytest.fixture
def delete_created_data():
    return _delete_created_data
