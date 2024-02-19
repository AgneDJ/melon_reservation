"""Server for melon app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import requests
import os
import json
import crud
from datetime import time, date, datetime, timedelta
import datetime as dt


from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY", None)
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def base():
    """View homepage."""
    return render_template("base.html")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host='0.0.0.0')
