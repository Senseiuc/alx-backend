#!/usr/bin/env python3
"""
A simple flask app demonstrating how to
display in different languages
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    A config class for configuring the languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Gets locale from request object
    """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello_world():
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
