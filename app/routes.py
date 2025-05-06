#!/usr/bin/env python3
from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Sam"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was pretty mid"},
        {
            "author": {"username": "BonzaiBuddy"},
            "body": "The purple monkey was cute until it gave my Windows XP machine a virus!",
        },
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
