import allure
from pydantic.error_wrappers import ValidationError
from source.enums.global_enums import GlobalError


class Assertion:

    def __init__(self, response):
        self.response = response
        self.json_data = response.json()
        self.status_code = response.status_code

    @allure.step('Assertion json by the model')
    def assert_json_by_model(self, model):
        try:
            if isinstance(self.json_data, list):
                for item in self.json_data:
                    model(**item)
            else:
                model(**self.json_data)
        except ValidationError as e:
            raise AttributeError(f"Could not map received object to pydantic model:\n{e.json()}")
        return self

    @allure.step('Assertion of a json key value')
    def assert_json_key_value(self, payload, key):
        assert self.json_data.get(key) == payload.get(key), GlobalError.INVALID_KEY_VALUE
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
