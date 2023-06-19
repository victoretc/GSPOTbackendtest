from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr


class Language(BaseModel):
    id: Optional[StrictInt] = Field(None, title='ID')
    name: StrictStr = Field(..., title='Name', min_length=1, max_length=100)
