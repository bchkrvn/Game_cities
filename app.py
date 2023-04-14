from flask import Flask, render_template

from game.views import game_blueprint


def create_app() -> Flask:
    application = Flask("app")
    application.register_blueprint(game_blueprint)

    @application.route('/')
    def main_page():
        return render_template('main.html')

    return application


app: Flask = create_app()

if __name__ == "__main__":
    app.run(debug=True)
