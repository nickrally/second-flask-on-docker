from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def hi():
    return jsonify(greeting="hi")
