from uuid import UUID
from typing import List
from pydantic import BaseModel, Field


class GameDLCLink(BaseModel):
    game: UUID = Field(..., title='Game')
    dlc: List[UUID]
