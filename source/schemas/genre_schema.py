from pydantic import BaseModel, StrictInt, StrictStr

from source.base.generator import Generator


class Genre(BaseModel):
    id: StrictInt = None
    name: StrictStr = ...

    @staticmethod
    def random(name=None, lang=None):
        if name is None:
            name = Generator(lang).get_word()
        return Genre(name=name)
