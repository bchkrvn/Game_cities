import json
import random

from constants import CITIES_PATH, RESULTS_PATH, BAD_LETTERS


class CitiesDAO:

    def __init__(self):
        self.cities_path = CITIES_PATH
        self.players = []
        self.path_result = RESULTS_PATH

    def get_cities(self) -> dict:
        """
        Загружает базу данных городов из файла cities.json
        :return: база городов (список словарей)
        """
        with open(self.cities_path, encoding='utf-8') as file:
            cities = json.load(file)

        return cities

    def is_city(self, city: str) -> bool:
        """
        Проверяет является ли введенное пользователем слово городом
        :param city: город игрока
        :param cities_data: база городов
        :return: bool
        """

        cities = self.get_cities()
        return city in cities[city[0]]

    def get_last_letter(self, word: str):
        """
        Позволяет получить последнюю букву города, за исключением букв, на которых нет городов
        :param word: город
        :return: последняя буква
        """
        for i in range(1, len(word)):
            if word[-i] not in BAD_LETTERS:
                return word[-i]

    def get_city(self, letter: str, used_cities):
        """
        Позволяет получить город из базы данных, которого не было в игре, на нужную букву
        :param letter: первая буква нужного города
        :param used_cities: список использованных городов
        :return: город
            """
        letter = letter.upper()
        cities = self.get_cities()

        while True:
            city = random.choice(cities[letter])
            if city not in used_cities:
                return city

    def get_prompt(self, letter: str, used_cities: list):
        """
        Позволяет получить подсказку, если пользователь не знает города
        :param letter: буква, на которую нужен город
        :param used_cities: список использованных городов
        :return: город
        """
        letter = letter.upper()
        cities = self.get_cities()

        while True:
            city = random.choice(cities[letter])
            if city not in used_cities:
                return city

    def get_first_city(self):
        """
        Позволяет получить первый город для начала игры
        :return: рандомный город
        """
        cities = self.get_cities()
        city_letter = random.choice(list(cities.keys()))
        return random.choice(cities[city_letter])

    def add_player(self, player):
        self.players.append(player)

    def get_player(self):
        if self.players:
            return self.players[-1]

    def get_cities_for_game(self, cities: list):
        results = []
        for i, city in enumerate(cities):
            if i % 2 == 0:
                results.append(['Компьютер', city])
            else:
                results.append(['Вы', city])

        return results

    def get_results(self):
        try:

            with open(self.path_result, encoding='utf-8') as file:
                results = json.load(file)

            results.sort(key=lambda result: result[1], reverse=True)
            return [[i, *result] for i, result in enumerate(results, 1)]

        except FileNotFoundError:
            return []
