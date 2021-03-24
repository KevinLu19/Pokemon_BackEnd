import re
from flask import Flask, abort, json
from flask_restful import Api, Resource, reqparse
from flask_jsonpify import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os
import database.pokemon_database_storage as pokemon_sql_data_base

app = Flask(__name__)
api = Api(app)
ma = Marshmallow(app)

# database directory require this.
PROJECT_ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# Configure SqlAlchemy
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pokemon.sqlite3"

# Create database
pokemon_database = SQLAlchemy(app)

# Marshmallow defining output format.
class PokemonSchema(ma.Schema):
    class Meta:
        fields = ("id", "pokemon_name", "pokemon_sprite_image")

pokemon_schema = PokemonSchema()
pokemon_schemas = PokemonSchema(many = True)

# # Required Parameters
# pokemon_requirement = reqparse.RequestParser()
# pokemon_requirement.add_argument("pokemon", type = "string", help = "Entering the Pokemon's name", required = "true")
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Pokemon(Resource):
    def get(self, pokemon_id):
        if pokemon_id < 0:
            # 400 status code = Bad Request response status code
            abort(400)

        # https://stackoverflow.com/questions/59721478/serializing-sqlalchemy-with-marshmallow
        data = pokemon_sql_data_base.PokemonDataBase.query.all()
        serializing_pokemon_data = pokemon_schemas.dump(data)

        request_pokemon_list = []

        for pokemon in serializing_pokemon_data:
            if pokemon["id"] == pokemon_id:
                print (pokemon["id"])
                request_pokemon_list.append(pokemon["id"])
                request_pokemon_list.append(pokemon["pokemon_name"])
                request_pokemon_list.append(pokemon["pokemon_sprite_image"])

        return request_pokemon_list

    def post(self, pokemon_name):
        return ""

# Separate the endpoints from the api to the actual front end game.
# Endpoints is a one ended communication channel to the server.
api.add_resource(Pokemon, "/api/pokemon/<int:pokemon_id>")
api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    app.run(debug=True)

    # # Testing database function.
    # test = pokemon_sql_data_base.PokemonDataBase()
    # print(test.grab_pokemon_data(170))

    # # Testing Sqlalchmey query function.
    # pokemon_database.session.query().filter_by(id=5).first()