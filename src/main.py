from flask import Flask, abort, json
from flask_restful import Api, Resource, reqparse
from flask_jsonpify import jsonify
from config import app, api

import database.database as pokemon_database
import os

# app = Flask(__name__)
# api = Api(app)

# # database directory require this.
# PROJECT_ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# Required Parameters
pokemon_requirement = reqparse.RequestParser()
pokemon_requirement.add_argument("pokemon", type = "string", help = "Entering the Pokemon's name", required = "true")
class Pokemon(Resource):
    def get(self, pokemon_name):
        if pokemon_name is None:
            # 400 status code = Bad Request response status code
            abort(400)

        query_pokemon_name = pokemon_database.PokemonDataBase()
        query_pokemon_name.check_user_guess_to_database(pokemon_name)

        return jsonify(query_pokemon_name, 200)

    def post(self, pokemon_name):
        return ""

# Separate the endpoints from the api to the actual front end game.
# Endpoints is a one ended communication channel to the server.
api.add_resource(Pokemon, "/api/pokemon/<string:pokemon_name>", endpoint = "pokemon_name")

# if __name__ == "__main__":
#     app.run(debug=True)

#     # tmp = pokemon_database.PokemonDataBase()
#     # tmp.print_items_in_database()
