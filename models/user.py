from dataclasses import dataclass


@dataclass
class User:
    username: str
    user_ip = str