from flask import Flask, render_template
import urllib.request, json


app = Flask(__name__)


@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])

@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("profile.html", profile=dict)

@app.route("/lista")
def get_list_characters():

    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict["results"]:
        character = {
        "name": character["name"],
        "status": character["status"],
        "species": character["species"],
        "gender": character["gender"],
        "location": character["location.name"],
        }
        characters.append(character)

    return {"characters": characters}
    

@app.route("/locations")
def get_locations():

    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)
    locations = response.read()
    dict = json.loads(locations)

    locations = []

    for location in dict["results"]:
        location = {
            "name": location["name"],
            "type": location["type"],
            "dimension": location["dimension"]
        }
        locations.append(location)
    return {"locations": locations}    
