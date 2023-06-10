from pydantic import BaseModel, Field, validator
from source.enums.global_enums import GlobalError


class Language(BaseModel):
    id: int
    name: str = Field(...)

    @validator('name')
    def validate_name_length(cls, value):
        if 1 > len(value) or len(value) > 100:
            raise ValueError(GlobalError.INVALID_STRING_LENGTH.value)
        return value