from flask import Flask, render_template, request

from .database import Session
from .models import Charity

app = Flask(__name__)
app.config.update({
    'TEMPLATES_AUTO_RELOAD': True,
    'DEBUG': True,
})


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        name = request.args.get("name", "World")
    elif request.method == "POST":
        name = request.form.get("name", "World")
    else:
        name = request.method

    return render_template("hello.html", name=name)


@app.route("/charity")
def charity_list():
    with Session() as db:
        charities = db.query(Charity).all()

    return render_template("charity_list.html", charities=charities)
