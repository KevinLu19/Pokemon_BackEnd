from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

import os

# creating flask app instance
app = Flask(__name__)
api = Api(app)

# database directory require this.
PROJECT_ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# Configure SqlAlchemy
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pokemon.sqlite3"

# Create database
pokemon_database = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)
