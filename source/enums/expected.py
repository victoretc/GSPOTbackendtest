from enum import Enum


class ExpectedJSON(Enum):
    NOT_FOUND = {
        "detail": "Страница не найдена."
    }
    FIELD_CANNOT_BE_EMPTY = ['Это поле не может быть пустым.']
    FIELD_CANNOT_CONTAINS_MORE_100 = ['Убедитесь, что это значение содержит не более 100 символов.']

    @staticmethod
    def key_value(key, value):
        json = {key: value}
        return json
