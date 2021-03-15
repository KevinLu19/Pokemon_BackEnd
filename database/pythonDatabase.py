from main import app
from flask_sqlalchemy import SQLAlchemy

import os
import re

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pokemon.sqlite3"

pokemon_database = SQLAlchemy(app)

class PokemonDataBase(pokemon_database.Model):
    id = pokemon_database.Column(pokemon_database.Integer, primary_key=True)
    pokemon_name = pokemon_database.Column(pokemon_database.String(15))
    pokemon_sprite_image = pokemon_database.Column(pokemon_database.String(10))

    def clearing_tables_in_database(self):
        # Clearing Tables in database.
        meta = pokemon_database.metadata

        for table in reversed(meta.sorted_tables):
            print('Clear table %s' % table)
            pokemon_database.session.execute(table.delete())
        pokemon_database.session.commit()

    # Temporary, to check if connection is still connected.
    def print_items_in_database(self):
        list_of_pokemon_names = grab_name_from_text_file()
        list_of_image_names = grab_image_name_from_sprite_directory()

        for poke_name, poke_image_name in zip(list_of_pokemon_names, list_of_image_names):
            print (poke_name)
            print(poke_image_name)
            print ("------------")


# Grabs pokemon's name from textfile and store them into a list to then place into databse.
def grab_name_from_text_file():

    pokemon_names_from_text_file = []

    with open ("pokemon_names.txt", "r") as f:
        pokemon_names = f.readlines()

    for item in pokemon_names:
        new_string = item.replace("\n", "")

        pokemon_names_from_text_file.append(new_string)

    return pokemon_names_from_text_file

def grab_image_name_from_sprite_directory():
    sprite_directory = "D:\Programming Workspace\PokemonGuessingGameBackEnd\sprites"
    file_sprities = os.listdir(sprite_directory)

    # Sorting the directory in a nifty yet working fashion.
    file_sprities.sort(key=lambda f: int(re.sub('\D', '', f)))

    return file_sprities
