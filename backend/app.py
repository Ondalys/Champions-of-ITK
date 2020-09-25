from flask import Flask, jsonify
from flask_cors import CORS
from dbconf import Config
from flask_sqlalchemy import SQLAlchemy

DEBUG = True

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import routes, models

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/roll', methods=['GET'])
def ping_pong(data):
    return jsonify(data)

if __name__ == '__main__':
    app.run()
