from typing import Optional, List
from pydantic import BaseModel, Field, StrictInt, StrictStr
from source.schemas.subgenre import Subgenre


class GenreGames(BaseModel):
    id: Optional[StrictInt] = Field(None, title='ID')
    name: StrictStr = Field(..., title='Name', min_length=1, max_length=50)
    subgenre: List[Subgenre]
