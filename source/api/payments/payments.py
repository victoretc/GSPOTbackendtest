import allure

from constants import tester_auth
from source.base.client import Requests
from source.enums.payments.payments import External_Payments


@allure.step('Get services list')
def get_services_list(auth=None):
    response = Requests.get(url=External_Payments.SERVICES, auth=auth)
    return response