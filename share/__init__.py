import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["BASE_URL"] = os.getenv("BASE_URL")

    from .models import db

    db.init_app(app)

    @app.context_processor
    def add_movie_variables():
        return dict(base_url=app.config["BASE_URL"])

    from share.views.movie import app as movie_app

    app.register_blueprint(movie_app)

    return app
