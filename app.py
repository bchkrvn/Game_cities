from flask import Flask, render_template

from config import config
from game.views import game_blueprint


def create_app(configuration) -> Flask:
    application = Flask("app")
    application.config.from_object(configuration)
    application.register_blueprint(game_blueprint)

    @application.route('/')
    def main_page():
        return render_template('main.html')

    return application


app: Flask = create_app(config)

if __name__ == "__main__":
    app.run(debug=True)
