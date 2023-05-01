from game.dao.cities import CitiesDAO
from models.cities import Cities
from models.game import Game
from models.result import ResultsDAO

cities = Cities()
cities_dao = CitiesDAO(cities)
results_dao = ResultsDAO()
game = Game(cities_dao=cities_dao, results_dao=results_dao)
