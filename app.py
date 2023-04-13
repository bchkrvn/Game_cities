from flask import Flask, render_template

from game.views import game_blueprint

app = Flask(__name__)

app.register_blueprint(game_blueprint)


@app.route('/')
def main_page():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)
