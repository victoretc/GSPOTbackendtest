from enum import Enum


class GlobalError(str, Enum):
    WRONG_STATUS_CODE = 'Status code is different than expected'
    INVALID_STRING_LENGTH = "Invalid string length"
    INVALID_KEY_VALUE = "The key value is different from the expected result"
    INVALID_JSON = "json is not equal to json"

    def __str__(self) -> str:
        return self.value
