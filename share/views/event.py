from flask import Blueprint, render_template, Response
from share.models import Movie

app = Blueprint("event_app", __name__, url_prefix="/events")


@app.route("/<string:slug>")
def movie_detail(slug):
    events = {
        "iim-rohtak-2024": {
            "title": "Moviepedia at IIM Rohtak | The Shorts Film Festival 2024 | Submit Your Film Now",
            "keywords": "IIM Rohtak 2024, IIM Rohtak, Moviepedia, Moviepediafilms, Moviepedia 2024",
            "about": "Are you an aspiring filmmaker looking to showcase your creativity and talent? IIM Rohtak, in collaboration with Moviepedia, presents an incredible opportunity for all budding filmmakers. Get your film screened and stand a chance to win cash prizes worth 40,000 INR!",
            "image": "img/events/iim-rohtak-2024-alt.png",
            "slug": slug,
            "poster": "img/events/iim-rohtak-2024-alt.png",
        }
    }
    meta = events.get(slug, None)
    if not meta:
        return Response("Not found", status=404)
    return render_template("events.html", meta=meta)
