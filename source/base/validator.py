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
    def assert_json_key_value(self, payload, key):
        assert self.response.json().get(key) == payload.get(key), GlobalError.INVALID_KEY_VALUE
        return self

    @allure.step('Assertion of a status code')
    def assert_status_code(self, expected: int):
        assert self.status_code == expected, GlobalError.WRONG_STATUS_CODE
        return self


def assert_json_by_model(response, model):
    return Assertion(response=response).assert_json_by_model(model=model)


def assert_json_key_value(response, payload, key):
    return Assertion(response=response).assert_json_key_value(payload=payload, key=key)


def assert_status_code(response, expected):
    return Assertion(response=response).assert_status_code(expected=expected)
