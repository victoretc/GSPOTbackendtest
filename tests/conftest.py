import pytest
import requests
from requests.auth import HTTPBasicAuth


def _delete_created_data(base_ulr, data_url, id_data):
    url_delete = base_ulr + data_url + str(id_data)
    response_delete = requests.delete(url=url_delete, auth=HTTPBasicAuth(username="tester", password="tester"))
    assert response_delete.status_code == 204


@pytest.fixture
def delete_created_data():
    return _delete_created_data
