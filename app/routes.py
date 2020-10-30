from flask import (render_template, request)
from app import app

@app.route("/")
def index():
    return "Generic index page\n"

