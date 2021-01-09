from flask import Blueprint, render_template
from share.models import MovieList

app = Blueprint("movie_list_app", __name__, url_prefix="/list")


@app.route("/<int:list_id>/<string:slug>/")
def movie_detail(list_id, slug):
    movie_list = MovieList.query.filter_by(id=list_id).first_or_404()
    return render_template("movie_list.html", movie_list=movie_list)
