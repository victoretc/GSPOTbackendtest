import allure
from pydantic.error_wrappers import ValidationError
from source.enums.global_enums import GlobalError


class Assertion:

    def __init__(self, response):
        self.response = response
        self.status_code = response.status_code

    def get_json(self):
        return self.response.json()

    @allure.step('Assertion json by the model')
    def assert_json_by_model(self, model):
        try:
            if isinstance(self.response.json(), list):
                for item in self.response.json():
                    model(**item)
            else:
                model(**self.response.json())
        except ValidationError as e:
            raise AttributeError(f"Could not map received object to pydantic model:\n{e.json()}")
        return self

    @allure.step('Assertion of a json key value')
    def assert_json_key_value(self, json, key):
        assert self.response.json().get(key) == json.get(key), f'{GlobalError.INVALID_KEY_VALUE}.\n' \
                                                               f'Expected: {json.get(key)}\n' \
                                                               f'Actual: {self.response.json().get(key)}' \
                                                               f'Response: {self.response.json()}'
        return self

    @allure.step('Assertion of a json equal json')
    def assert_json_equal_json(self, json):
        assert self.response.json() == json, f'{GlobalError.INVALID_JSON}.\n'\
                                             f'Response: {self.response.json()}'
        return self

    @allure.step('Assertion of a status code')
    def assert_status_code(self, expected: int):
        assert self.status_code == expected, f'{GlobalError.WRONG_STATUS_CODE}.\n' \
                                             f'Expected: {expected}\n'\
                                             f'Actual: {self.status_code}\n'
        return self


def assert_json_by_model(response, model):
    return Assertion(response=response).assert_json_by_model(model=model)


def assert_json_key_value(response, json, key):
    return Assertion(response=response).assert_json_key_value(json=json, key=key)


def assert_json_equal_json(response, json):
    return Assertion(response=response).assert_json_equal_json(json=json)


def assert_status_code(response, expected):
    return Assertion(response=response).assert_status_code(expected=expected)
