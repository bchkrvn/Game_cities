class NotAlpha(Exception):
    def __init__(self):
        self.message = f'Название города должно состоять из букв'


class UsedCity(Exception):
    def __init__(self, city):
        self.message = f'Город {city} уже был использован в этой игре'


class IsNotCity(Exception):
    def __init__(self, city):
        self.message = f'{city} не является российским городом'


class WrongLetter(Exception):
    def __init__(self, wrong_letter: str, right_letter: str):
        self.message = f'Вы назвали город на букву  "{wrong_letter.upper()}", ' \
                       f'а нужно было на букву "{right_letter.upper()}"'
