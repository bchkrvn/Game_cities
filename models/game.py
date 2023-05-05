from constants import BAD_LETTERS, RUSSIAN_LETTERS
from exceptions import UsedCity, IsNotCity, WrongLetter, NotAlpha
from game.dao.cities import CitiesDAO
from models.result import ResultsDAO
from models.user import User


class Game:
    def __init__(self, cities_dao: CitiesDAO, results_dao: ResultsDAO):
        self._cities_dao = cities_dao
        self._user: None or User = None
        self._results_dao = results_dao

    def set_user(self, username: str) -> None:
        self._user = User(username=username, used_cities=list())

    def del_user(self) -> None:
        self._user = None

    def get_last_city(self) -> str:
        return self._user.used_cities[-1]

    def get_last_letter(self, city: str) -> str:
        city.lower()
        for i in range(1, len(city)):
            if city[-i] not in BAD_LETTERS:
                return city[-i]

    def validate_user_city(self, user_city: str) -> None:
        if not set(user_city) <= RUSSIAN_LETTERS:
            raise NotAlpha()

        if not self._cities_dao.is_city(user_city):
            raise IsNotCity(user_city)

        if user_city in self._user.used_cities:
            raise UsedCity(user_city)

        last_city = self.get_last_city()
        last_letter = self.get_last_letter(last_city)
        user_city_first_letter = user_city[0]
        if last_letter != user_city_first_letter:
            raise WrongLetter(user_city_first_letter, last_letter)

    def add_city_to_used(self, city: str) -> None:
        self._user.used_cities.append(city)

    def get_data(self) -> dict or None:
        data = {}
        last_city = self.get_last_city()
        letter = self.get_last_letter(last_city)
        cities_by_letter = self._cities_dao.get_shuffle_cities_by_letter(letter)

        for city in cities_by_letter:
            if city not in self._user.used_cities:
                self._user.used_cities.append(city)
                data['letter'] = self.get_last_letter(city).upper()
                break
        else:
            return None

        data['used_cities_and_players'] = self.get_used_cities_and_players_for_data()
        data['used_cities'] = list(map(lambda x: x.capitalize(), self._user.used_cities))
        return data

    def get_data_error(self) -> dict:
        data = {}
        last_city = self.get_last_city()
        letter = self.get_last_letter(last_city)
        data['letter'] = letter.upper()
        data['used_cities_and_players'] = self.get_used_cities_and_players_for_data()
        data['used_cities'] = self._user.used_cities

        return data

    def get_first_data(self) -> dict:
        if self._user.used_cities:
            return self.get_data_error()

        data = {}
        first_city = self._cities_dao.get_random_city()
        self._user.used_cities.append(first_city)
        data['letter'] = self.get_last_letter(first_city).upper()
        data['used_cities_and_players'] = self.get_used_cities_and_players_for_data()
        data['used_cities'] = self._user.used_cities
        return data

    def get_used_cities_and_players_for_data(self):
        results = []
        for i, city in enumerate(self._user.used_cities[-6:]):
            if i % 2 == 0:
                results.append(['Компьютер', city.capitalize()])
            else:
                results.append(['Вы', city.capitalize()])

        return results

    def end_game(self):
        points = self._user.get_result()
        username = self._user.username
        self._results_dao.save_result(username, points)
        data = {'username': username,
                'result': points}
        return data

    def get_results(self):
        results = self._results_dao.get_results()
        data = {
            'top3': results[:3],
            'top10': results[3:10]
        }
        return data
