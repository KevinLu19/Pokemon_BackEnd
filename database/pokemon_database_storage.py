from flask_sqlalchemy import SQLAlchemy
from Pokemon_resource_api import pokemon_database, PROJECT_ROOT_DIRECTORY, pokemon_schemas

import os
import re

class PokemonDataBase(pokemon_database.Model):
    id = pokemon_database.Column(pokemon_database.Integer, primary_key=True)
    pokemon_name = pokemon_database.Column(pokemon_database.String(15))
    pokemon_sprite_image = pokemon_database.Column(pokemon_database.String(10))

    # DANGEROUS METHOD. PROCEED WITH CAUTION!
    def clearing_tables_in_database(self):
        # Clearing Tables in database.
        meta = pokemon_database.metadata

        for table in reversed(meta.sorted_tables):
            print('Clear table %s' % table)
            pokemon_database.session.execute(table.delete())
        pokemon_database.session.commit()

    # When doing name comparison to the database.
    # Take the given name from user and lower case it before doing the comparision with the database.
    def check_user_guess_to_database(self, user_guessed_name: int):
        # user_guess_lower_cased = user_guessed_name.lower()

        # https://stackoverflow.com/questions/32938475/flask-sqlalchemy-check-if-row-exists-in-table
        # The filter_by() parameter uses the column table's name to sift through what data you are trying to query out.
        # This returns a boolean if left with "is not None" at the end.
        return pokemon_database.session.query(PokemonDataBase.pokemon_name).filter_by(id = user_guessed_name).first()

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
    image_sprite_directory_path = os.path.join(PROJECT_ROOT_DIRECTORY, "sprites")
    file_sprities = os.listdir(image_sprite_directory_path)

    # Sorting the directory in a nifty yet working fashion.
    # Found this solution at https://stackoverflow.com/questions/33159106/sort-filenames-in-directory-in-ascending-order
    file_sprities.sort(key=lambda f: int(re.sub('\D', '', f)))

    return file_sprities