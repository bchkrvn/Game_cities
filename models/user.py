from dataclasses import dataclass


@dataclass
class User:
    username: str
    used_cities: list[str]

    def __repr__(self):
        return self.username

    def get_result(self):
        return len(self.used_cities) // 2
