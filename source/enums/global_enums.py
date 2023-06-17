from enum import Enum


class GlobalError(str, Enum):
    WRONG_STATUS_CODE = 'Status code is different than expected'
    INVALID_STRING_LENGTH = "Invalid string length"

    def __str__(self) -> str:
        return self.value
