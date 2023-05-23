#!/usr/bin/env python3
"""
Basic babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    Return html file in / route
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
