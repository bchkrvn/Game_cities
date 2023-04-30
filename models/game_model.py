class Game:
    def __init__(self):
        self._username = None
        self.used_city = []

    def set_username(self, username):
        self._username = username

    def add_user_city(self, user_city):
