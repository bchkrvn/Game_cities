import json
import datetime

from constants import RESULTS_PATH


class GameDAO:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.result_path = RESULTS_PATH
        self.used_cities = []

    def add_point(self):
        self.points += 1

    def save_result(self):
        try:
            with open(self.result_path, encoding='utf-8') as file:
                results = json.load(file)
        except:
            results = []

        results.append([self.name, self.points, f'{datetime.datetime.now()}'])

        with open(self.result_path, 'w', encoding='utf-8') as file:
            json.dump(results, file)

    def is_new_game(self):
        return not bool(self.used_cities)

    def get_used_cities(self):
        return self.used_cities

    def get_name(self):
        return self.name

    def get_result(self):
        return self.points

    def is_used_city(self, city: str):
        return city in self.used_cities

    def add_used_city(self, city_1, city_2):
        self.used_cities.append(city_1)
        self.used_cities.append(city_2)
        self.add_point()

    def add_city(self, city: str):
        self.used_cities.append(city)