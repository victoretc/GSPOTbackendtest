from faker import Faker


class Generator:
    Faker.seed(1)

    def __init__(self, lang=None):
        self.fake = Faker(lang)
        self.language = None
        self.word = None

    def get_language(self):
        self.language = self.fake.language_name()
        return self.language

    def get_word(self):
        self.word = self.fake.word()
        return self.word
