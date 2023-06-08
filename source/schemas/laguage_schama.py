from typing import List
from pydantic import BaseModel, Field


class Language(BaseModel):
    id: int
    name: str
