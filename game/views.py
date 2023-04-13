from flask import Blueprint, render_template, request, redirect
from .dao.cities_dao import CitiesDAO
from .dao.game_dao import GameDAO

game_blueprint = Blueprint('game_blueprint', __name__, template_folder='templates')

cities_dao = CitiesDAO()


@game_blueprint.route('/user_name')
def start_game():
    user_name = request.args.get('user_name')
    if user_name:
        user = GameDAO(user_name.capitalize())
        cities_dao.add_player(user)
        return redirect('/game')
    else:
        return render_template('user_name.html')


@game_blueprint.route('/game')
def game():
    user = cities_dao.get_player()
    if user.is_new_game():
        first_city = cities_dao.get_first_city()
        user.add_city(first_city)

    cities = user.get_used_cities()
    cities_for_game = cities_dao.get_cities_for_game(cities)

    last_letter = cities_dao.get_last_letter(cities[-1])

    return render_template('game.html', cities=cities_for_game, last_letter=last_letter)


@game_blueprint.route('/user_city')
def user_answer():
    user_city = request.args.get('user_city')
    user_city = user_city.capitalize()

    if not user_city.isalpha():
        message = 'Город должен состоять из букв, попробуйте еще раз'
        return render_template('error.html', message=message)

    if not cities_dao.is_city(user_city):
        message = 'Вы ввели не город, попробуйте еще раз'
        return render_template('error.html', message=message)

    user = cities_dao.get_player()
    if user.is_used_city(user_city):
        message = 'Этот город уже был, попробуйте еще раз'
        return render_template('error.html', message=message)

    last_city = user.get_used_cities()[-1]
    last_letter = cities_dao.get_last_letter(last_city)

    if not user_city[0].lower() == last_letter:
        message = f'Вам нужно ввести город на букву {last_letter.upper()}, попробуйте еще раз'
        return render_template('error.html', message=message)

    user_last_letter = cities_dao.get_last_letter(user_city)

    program_city = cities_dao.get_city(user_last_letter, user.get_used_cities())
    user.add_used_city(user_city, program_city)

    return redirect('/game')


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
