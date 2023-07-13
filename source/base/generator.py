import allure
from faker import Faker


class Generator:

    @staticmethod
    @allure.step('Generating data based on json model {model}')
    def object(model=None, lang=None, seed=None, include=None, exclude=None, **field_values):
        """
        :param model: Pydantic model according to which data will be generated.
        :param lang: The language for generating data in the "ru_RU" format.
        :param seed: Provides reproducibility of generated data when using the same seed value.
        :param include: Allows specifying the fields to be included in the data. It can be used as: 'key' or {'key1', 'key2'}.
        :param exclude: Allows specifying the fields to be excluded from the data. It can be used as: 'key' or {'key1', 'key2'}.
        :param field_values: Allows setting custom field values. It can be used as: key=1, key2='value'.
        :return: A dictionary with generated values.
        """
        Faker.seed(seed)
        fake = Faker(lang)
        data = {}
        for key in model.__fields__:
            if exclude and key in exclude:
                continue
            if include and key not in include:
                continue
            if key in field_values:
                data[key] = field_values[key]
            else:
                if key == 'name':
                    data[key] = fake.word()
                elif key == 'languageName':
                    data[key] = fake.language_name()
                elif key == 'interface':
                    data[key] = fake.boolean()
                elif key == 'subtitles':
                    data[key] = fake.boolean()
                elif key == 'voice':
                    data[key] = fake.boolean()
                elif key == 'operatingSystem':
                    data[key] = 'WINDOWS'
                elif key == 'deviceProcessor':
                    data[key] = fake.word()
                elif key == 'deviceStorage':
                    data[key] = fake.word()
                elif key == 'deviceGraphics':
                    data[key] = fake.word()
                elif key == 'typeRequirements':
                    data[key] = 'RECOMMEND'
        return data
