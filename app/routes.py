from app import app  # , db
from app.forms import SignButton, SignForm, ReadButton
from flask import render_template, redirect, url_for, session, request


@app.route("/", methods=["GET", "POST"])
def start_page():
    signbutton = SignButton()
    if signbutton.validate_on_submit():
        return redirect(url_for("sign_form"))
    return render_template("start_page.html", signbutton=signbutton)


@app.route("/introduction", methods=["GET", "POST"])
def intro_page():
    readbutton = ReadButton()
    if readbutton.validate_on_submit():
        return redirect(url_for("start_page"))
    return render_template("intro_page.html", readbutton=readbutton)


@app.route("/sign_form", methods=["GET", "POST"])
def sign_form():
    signform = SignForm()
    if signform.validate_on_submit():
        print("Yoyoyo")
    else:
        print(signform.errors)
    return render_template("sign_form_page.html", signform=signform)
