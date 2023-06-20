import allure
from faker import Faker


class Generator:

    @staticmethod
    @allure.step(f'Generating data based on json model')
    def object(model=None, lang=None, seed=None, include=None, exclude=None, **field_values):
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
                if key == 'id':
                    data[key] = fake.random_digit_not_null()
                elif key == 'name':
                    data[key] = fake.word()
        return data
