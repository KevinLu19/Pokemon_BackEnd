#import database.pokemon_database_storage
import requests
import random

def choose_number():
    random_generator = random.randint(1, 2)
    return random_generator

BASE_URL = "http://127.0.0.1:5000/"

# rando_number = choose_number()

# user_input = input("Enter pokemon name: ")

# response = requests.get(BASE_URL + f"pokemon/4")
response = requests.get(BASE_URL)
#response = requests.get(BASE_URL + "hello_world")

print (response.json())

# if __name__ == "__main__":
#     test = database.database.PokemonDataBase()
#     test.check_user_guess_to_database("charmander")