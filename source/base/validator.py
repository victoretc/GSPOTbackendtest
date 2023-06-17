from pydantic.error_wrappers import ValidationError
from source.enums.global_enums import GlobalError


class ResponseValidator:

    def __init__(self, response):
        self.response = response
        self.json_response = response.json()
        self.status_code = response.status_code
        self.parsed_object = None

    def validate(self, schema):
        try:
            if isinstance(self.json_response, list):
                for item in self.json_response:
                    parsed_object = schema.parse_obj(item)
                    self.parsed_object = parsed_object
            else:
                schema.parse_obj(self.json_response)
        except ValidationError:
            raise AttributeError("Could not map received object to pydantic schema")

    def assert_status_code(self, status_code: int):
        assert self.status_code == status_code, GlobalError.WRONG_STATUS_CODE
        return self

    def __str__(self):
        return \
            f"\nStatus code: {self.status_code} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.json_response}"
