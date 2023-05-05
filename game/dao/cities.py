import random

from models.cities import Cities


class CitiesDAO:

    def __init__(self, cities: Cities):
        self.cities = cities

    def is_city(self, user_city: str) -> bool:
        return user_city.lower() in self.cities.get_cities_by_letter(user_city[0].lower())

    def get_shuffle_cities_by_letter(self, letter: str):
        cities = self.cities.get_cities_by_letter(letter)
        random.shuffle(cities)
        return cities

    def get_random_city(self) -> str:
        cities_by_letter = random.choice(list(self.cities.get_all_cities().values()))
        return random.choice(cities_by_letter)
