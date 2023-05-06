from flask import Blueprint, render_template, request, redirect

from container import games, result
from exceptions import UsedCity, IsNotCity, WrongLetter, NotAlpha
from models.game import Game

game_blueprint = Blueprint('game_blueprint', __name__, template_folder='templates')


@game_blueprint.get('/user_name')
def get_username():
    return render_template('user_name.html')


@game_blueprint.post('/user_name')
def post_username():
    username = request.values.get('user_name')
    ip = request.remote_addr
    games[ip] = Game()
    games[ip].set_user(username.capitalize())
    return redirect('/start_game')


@game_blueprint.get('/start_game')
def start_game():
    game = games.get(request.remote_addr, None)
    if not game:
        return redirect('/user_name')

    data_for_template = game.get_first_data()
    return render_template('game.html', data=data_for_template)


@game_blueprint.post('/game')
def user_answer():
    game = games.get(request.remote_addr, None)
    if not game:
        return redirect('/user_name')

    user_city = request.values.get('user_city').lower()

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


@game_blueprint.get('/game')
def show_game():
    game = games.get(request.remote_addr, None)
    if not game:
        return redirect('/user_name')

    data_for_template = game.get_data_error()

    return render_template('game.html', data=data_for_template)


@game_blueprint.get('/game_over')
def game_over():
    game = games.get(request.remote_addr, None)
    if not game:
        return redirect('/user_name')

    data = game.end_game()
    del games[request.remote_addr]
    return render_template('game_over.html', data=data)


@game_blueprint.get('/results')
def results():
    data = result.get_results()
    return render_template('results.html', data=data)
