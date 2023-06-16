from enum import Enum

BASE_URL = "https://games.alpha.g-spot.website/api/v1/"


class Community(str, Enum):
    COMMENTS = f'{BASE_URL}community/comments/'
    REVIEW = f'{BASE_URL}community/review/'

    def __str__(self) -> str:
        return self.value


class Core(str, Enum):
    DLC = f'{BASE_URL}core/dlc/'
    PRODUCT = f'{BASE_URL}core/product'
    PRODUCTS = f'{BASE_URL}core/products/'
    SYSTEM_REQUIREMENT = f'{BASE_URL}core/system_requirement/'

    def __str__(self) -> str:
        return self.value


class Reference(str, Enum):
    GENRE = f'{BASE_URL}reference/genre/'
    LANGUAGES = f'{BASE_URL}reference/languages/'
    PRODUCT_LANGUAGES = f'{BASE_URL}reference/product_languages/'
    SUBGENRE = f'{BASE_URL}reference/subgenre/'

    def __str__(self) -> str:
        return self.value


class Utils(str, Enum):
    GENRES = f'{BASE_URL}utils/filters/genres/'
    PLATFORMS = f'{BASE_URL}utils/filters/platforms/'
    PRICES = f'{BASE_URL}utils/filters/prices/'

    def __str__(self) -> str:
        return self.value
