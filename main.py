from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model

from src import pokedex

import database.pythonDatabase as pokemon_database
import os, re

app = Flask(__name__)
api = Api(app)

# database directory require this.
PROJECT_ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# Required Parameters
pokemon_requirement = reqparse.RequestParser()
pokemon_requirement.add_argument("pokemon", type = "string", help = "Entering the Pokemon's name", required = "true")
class Pokemon(Resource):
    def get(self):
        # return pokedex.pokedex
        return ""

    def post(self, pokemon_name):
        return ""

# Separate the endpoints from the api to the actual front end game.
# Endpoints is a one ended communication channel to the server.
api.add_resource(Pokemon, "/api/pokemon/<int:pokemon_id>", endpoint = "pokemon_id")


if __name__ == "__main__":
    # app.run(debug=True)

    tmp = pokemon_database.PokemonDataBase()
    tmp.print_items_in_database()
