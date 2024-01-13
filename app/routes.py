from app import app  # , db

from flask import render_template, redirect, url_for, session, request


@app.route("/", methods=["GET", "POST"])
def start_page():
    return render_template("start_page.html")
