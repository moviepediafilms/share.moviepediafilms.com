from flask import Blueprint, render_template
from share.models import Movie

app = Blueprint("movie_app", __name__, url_prefix="/movie")


@app.route("/<int:movie_id>/<string:slug>/")
def movie_detail(movie_id, slug):
    movie = Movie.query.filter_by(id=movie_id).first_or_404()
    return render_template("movie.html", title="Welcome to flask", movie=movie)
