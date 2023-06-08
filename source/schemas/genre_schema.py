from typing import List
from pydantic import BaseModel, Field


class Genre(BaseModel):
    id: int
    name: str
