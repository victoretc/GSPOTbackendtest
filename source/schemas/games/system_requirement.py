from enum import Enum
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, StrictStr


class OperatingSystemEnum(Enum):
    LINUX = 'LINUX'
    WINDOWS = 'WINDOWS'
    MACOS = 'MACOS'
    PS = 'PS'
    XBOX = 'XBOX'


class TypeRequirementsEnum(Enum):
    MINIMUM = 'MINIMUM'
    RECOMMEND = 'RECOMMEND'


class SystemRequirement(BaseModel):
    id: Optional[UUID] = Field(None, title='Id')
    operatingSystem: OperatingSystemEnum = Field(..., title='Operation system')
    deviceProcessor: StrictStr = Field(..., title='Processor', min_length=1, max_length=100)
    deviceMemory: StrictStr = Field(..., title='Memory', min_length=1, max_length=100)
    deviceStorage: StrictStr = Field(..., title='Storage', min_length=1, max_length=100)
    deviceGraphics: StrictStr = Field(..., title='Graphics', min_length=1, max_length=100)
    typeRequirements: TypeRequirementsEnum = Field(..., title='System requirement')
