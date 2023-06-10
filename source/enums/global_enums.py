from enum import Enum


class GlobalError(Enum):
    WRONG_STATUS_CODE = 'Status code is different than expected'
    INVALID_STRING_LENGTH = "Invalid string length"
