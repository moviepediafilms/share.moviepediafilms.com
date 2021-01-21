from flask import Blueprint, render_template


app = Blueprint("catch_all_app", __name__, url_prefix="")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("base.html")
