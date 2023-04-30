from game.dao.cities import CitiesDAO
from models.cities import Cities
from models.game import Game

cities = Cities()
cities_dao = CitiesDAO(cities)
game = Game(cities_dao)
