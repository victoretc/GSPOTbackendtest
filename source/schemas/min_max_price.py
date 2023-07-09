from typing import Optional
from pydantic import BaseModel, Field, StrictStr


class MinMaxPrice(BaseModel):
    minPrice: Optional[str] = Field(None, title='Min price')
    maxPrice: Optional[str] = Field(None, title='Max price')
