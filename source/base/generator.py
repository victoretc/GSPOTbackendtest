from faker import Faker

class Generator:

    def __init__(self, lang=None):
        self.fake = Faker(lang)
        self.language = None

    def get_language(self):
        self.language = self.fake.language_name()
        return self.language
