import requests
import random

def choose_number():
    random_generator = random.randint(1, 2)
    return random_generator

BASE_URL = "http://127.0.0.1:5000/"

rando_number = choose_number()

response = requests.get(BASE_URL + f"pokemon/{rando_number}")
#response = requests.get(BASE_URL + "hello_world")

print (response.json())