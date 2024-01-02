from flask import Blueprint, render_template, Response
from share.models import Movie

app = Blueprint("event_app", __name__, url_prefix="/events")


@app.route("/<string:slug>")
def movie_detail(slug):
    events = {
        "iim-rohtak-2024": {
            "title": "IIM Rohtak 2024",
            "keywords": "IIM Rohtak 2024, IIM Rohtak, Moviepedia, Moviepediafilms, Moviepedia 2024",
            "about": "IIM Rohtak 2024 is a movie event organized by Moviepediafilms. It is a movie event for the students across the country.",
            "image": "img/events/iim-rohtak-2024.png",
            "slug": slug,
            "poster": "img/events/iim-rohtak-2024.png",
        }
    }
    meta = events.get(slug, None)
    if not meta:
        return Response("Not found", status=404)
    return render_template("events.html", meta=meta)
