from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class Note(db.Model):
    __tablename__ = "note"

    id = db.Column(db.Integer, primary_key=True)
    english = db.Column(db.Text)
    spanish = db.Column(db.Text)

    def __init__(self, english, spanish):
        self.english = english
        self.spanish = spanish


@app.route("/")
def hi():
    return jsonify(greeting="hello there")
