"""Models for Melons app."""

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'user'

    user_name = db.Column(db.String)
    email = db.Column(db.String, primary_key=True)

    def __repr__(self):
        return f'<User user_id={__blank__} >'


class Reservations(db.Model):
    """Reservations."""

    __tablename__ = 'reservation'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, db.ForeignKey("user.email"))
    reservation = db.Column(db.String)

    email = db.relationship('User', back_populates="reservation")

    def __repr__(self):
        return f'<User user_id={__blank__} >'


def connect_to_db(flask_app, db_uri="postgresql:///user", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)

    with app.app_context():
        db.create_all()
