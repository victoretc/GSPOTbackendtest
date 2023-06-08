import requests
from .constants import BASE_URL
import allure 

@allure.story('Проверка успешного ответа [404] при отправке запроса на главную страницу')
def test_main_page():
    with allure.step('Отправка запроса'):
        response = requests.get(BASE_URL)
    with allure.step('Проверяем что код ответа равен 404'):
        assert response.status_code == 404



