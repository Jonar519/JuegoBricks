import requests

def obtener_chiste_aleatorio():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    return response.json()["value"]