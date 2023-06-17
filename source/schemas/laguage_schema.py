from pydantic import BaseModel, StrictInt, StrictStr
from source.base.generator import Generator


class Language(BaseModel):
    id: StrictInt = None
    name: StrictStr = ...

    @staticmethod
    def random(name=None, lang=None):
        if name is None:
            name = Generator(lang).get_language()
        return Language(name=name)

