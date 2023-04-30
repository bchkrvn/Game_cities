from flask import Blueprint, render_template, request, redirect

from container import game
from exceptions import UsedCity, IsNotCity, WrongLetter, NotAlpha
from .dao.cities_dao import CitiesDAOold
from .dao.game_dao import GameDAO

game_blueprint = Blueprint('game_blueprint', __name__, template_folder='templates')

cities_dao = CitiesDAOold()


@game_blueprint.get('/user_name')
def get_username():
    return render_template('user_name.html')


@game_blueprint.post('/user_name')
def post_username():
    username = request.values.get('user_name')
    game.set_user(username.capitalize())
    # user = GameDAO(user_name.capitalize())
    # cities_dao.add_player(user)
    return redirect('/start_game')


@game_blueprint.route('/start_game')
def start_game():
    data_for_template = game.get_first_data()
    return render_template('game.html', data=data_for_template)


@game_blueprint.post('/game')
def user_answer():
    user_city = request.values.get('user_city').capitalize()

    try:
        game.validate_user_city(user_city)
    except (NotAlpha, UsedCity, IsNotCity, WrongLetter) as e:
        data_for_template = game.get_data_error()
        data_for_template['error'] = e.message
        return render_template('game.html', data=data_for_template)
        # return render_template('error.html', message=e.message)

    game.add_city_to_used(user_city)
    data_for_template = game.get_data()

    return render_template('game.html', data=data_for_template)


@game_blueprint.route('/game_over')
def game_over():
    user = cities_dao.get_player()
    user.save_result()
    name = user.get_name()
    result = user.get_result()
    return render_template('game_over.html', result=result, name=name)


@game_blueprint.route('/results')
def results():
    all_results = cities_dao.get_results()

    return render_template('results.html', results=all_results)
