from enum import Enum
from pydantic import BaseModel
from typing import List


class OperatingSystemEnum(Enum):
    LINUX = "Linux"
    WINDOWS = "Windows"
    MACOS = "MacOS"
    PS = "PS"
    XBOX = "XBOX"


class OperatingSystem(BaseModel):
    """Пустая модель в свагере?"""
    operatingSystem: List[OperatingSystemEnum]
