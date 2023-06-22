from typing import Optional
from pydantic import BaseModel, Field, StrictStr, StrictInt, StrictBool


class ProductLanguages(BaseModel):
    id: Optional[StrictInt] = Field(None, title='ID')
    languageName: StrictStr = Field(..., title='Language name', min_length=1)
    interface: Optional[StrictBool] = Field(None, title='Interface')
    subtitles: Optional[StrictBool] = Field(None, title='Subtitles')
    voice: Optional[StrictBool] = Field(None, title='Voice')
