from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr


class Subgenre(BaseModel):
    id: Optional[StrictInt] = Field(None, title='ID')
    name: StrictStr = Field(..., title='Subgenre', min_length=1, max_length=50)
