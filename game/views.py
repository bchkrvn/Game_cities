from flask import Blueprint, render_template, request, redirect

from container import game
from exceptions import UsedCity, IsNotCity, WrongLetter, NotAlpha
from .dao.cities_dao import CitiesDAOold

game_blueprint = Blueprint('game_blueprint', __name__, template_folder='templates')

cities_dao = CitiesDAOold()


@game_blueprint.get('/user_name')
def get_username():
    return render_template('user_name.html')


@game_blueprint.post('/user_name')
def post_username():
    username = request.values.get('user_name')
    game.set_user(username.capitalize())
    return redirect('/start_game')


@game_blueprint.get('/start_game')
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

    game.add_city_to_used(user_city)
    data_for_template = game.get_data()

    if not data_for_template:
        return redirect('/game_over')

    return render_template('game.html', data=data_for_template)


@game_blueprint.route('/game_over')
def game_over():
    data = game.end_game()
    return render_template('game_over.html', data=data)


@game_blueprint.route('/results')
def results():
    data = game.get_results()
    return render_template('results.html', data=data)
