#!/usr/bin/env python3
"""
Module to Parametrize templates
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import List, Optional, Dict


class Config:
    """
    Class for Flask Babel configuration.
    """
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users: Dict[int, Dict[str, Optional[str]]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """
    Return locale from request or default behavior.
    """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user(user_id: int) -> Optional[Dict[str, Optional[str]]]:
    """
    Return user dictionary based on user ID.
    """
    return users.get(user_id)


@app.before_request
def before_request() -> None:
    """
    Set the user as a global on flask.g.user.
    """
    user_id = request.args.get("login_as")
    g.user = get_user(int(user_id)) if user_id else None


@app.route("/")
def index() -> str:
    """
    Return welcome message based on user login status.
    """
    if g.user:
        return render_template(
            "5-index.html",
            message=gettext("logged_in_as") % {"username": g.user["name"]}
        )
    else:
        return render_template("5-index.html", message=gettext("not_logged_in"))


if __name__ == "__main__":
    app.run(debug=True)
