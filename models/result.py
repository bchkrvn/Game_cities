from dataclasses import dataclass
from datetime import datetime

from models.user import User


@dataclass
class Result:
    username: User
    points: int
    date: datetime

    def get_date(self):
        return self.date.strftime("%d/%m/%y")
