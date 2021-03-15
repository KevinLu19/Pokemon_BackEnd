from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model

from src import pokedex

import database.pythonDatabase as pokemon_database
import os, re

app = Flask(__name__)
api = Api(app)
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pokemon.sqlite3"

# pokemon_database = SQLAlchemy(app)

# class PokemonDataBase(pokemon_database.Model):
#     id = pokemon_database.Column(pokemon_database.Integer, primary_key=True)
#     pokemon_name = pokemon_database.Column(pokemon_database.String(15))
#     pokemon_sprite_image = pokemon_database.Column(pokemon_database.String(10))


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

# Temporary stuff. Trying to initially fill up the database.
def grab_name_from_text_file():

    pokemon_names_from_text_file = []

    with open ("pokemon_names.txt", "r") as f:
        pokemon_names = f.readlines()

    for item in pokemon_names:
        new_string = item.replace("\n", "")

        pokemon_names_from_text_file.append(new_string)

    return pokemon_names_from_text_file

if __name__ == "__main__":
    # app.run(debug=True)

    # Temporary stuff. Trying to initially fill up the database.
    # list_of_pokemon_names = grab_name_from_text_file()

    # sprite_directory = "D:\Programming Workspace\PokemonGuessingGameBackEnd\sprites"
    # file_sprities = os.listdir(sprite_directory)

    # file_sprities.sort(key=lambda f: int(re.sub('\D', '', f)))

    # for poke_name, poke_image_name in zip(list_of_pokemon_names, file_sprities):
    #     print(poke_name)
    #     print(poke_image_name)
    #     print("=======")


    # # Clearing Tables in database.
    # meta = pokemon_database.metadata

    # for table in reversed(meta.sorted_tables):
    #     print('Clear table %s' % table)
    #     pokemon_database.session.execute(table.delete())
    # pokemon_database.session.commit()

    # for poke_names, poke_image_names in zip(list_of_pokemon_names, file_sprities):
    #     pokemon_row = PokemonDataBase(pokemon_name= poke_names, pokemon_sprite_image = poke_image_names)
    #     pokemon_database.session.add(pokemon_row)

    # pokemon_database.session.commit()


    tmp = pokemon_database.PokemonDataBase()
    tmp.print_items_in_database()
