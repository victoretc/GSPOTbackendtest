from pydantic import BaseModel
from typing import List

from source.schemas.games.system_requirement import OperatingSystemEnum


class OperatingSystem(BaseModel):
    """Пустая модель в свагере?"""
    operatingSystem: List[OperatingSystemEnum]
