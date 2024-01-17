from app import app  # , db
from app.forms import SignButton
from flask import render_template, redirect, url_for, session, request


@app.route("/", methods=["GET", "POST"])
def start_page():
    signbutton = SignButton()
    return render_template("start_page.html", signbutton=signbutton)
