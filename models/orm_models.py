import json
from dataclasses import dataclass
from datetime import datetime

from constants import CITIES_PATH


class Cities:
    def __init__(self):
        self._cities = self._load_cities()

    def _load_cities(self):
        with open(CITIES_PATH) as file:
            cities: dict = json.load(file)

        return cities


@dataclass
class Result:
    username: str
    date: datetime

    def get_date(self):
        return self.date.strftime("%d/%m/%y")
