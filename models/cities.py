import json

from constants import CITIES_PATH
from models.base_singltone import BaseSingleton


class Cities(metaclass=BaseSingleton):
    def __init__(self):
        self._cities = self._load_cities()

    def _load_cities(self) -> dict[str:list]:
        with open(CITIES_PATH) as file:
            cities: dict = json.load(file)

        return cities

    def get_all_cities(self) -> dict:
        return self._cities

    def get_cities_by_letter(self, letter: str) -> list or None:
        return self._cities.get(letter.upper(), None)

