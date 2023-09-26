from flask import Flask, render_template
import urllib.request, json


app = Flask(__name__)


@app.route("/")
def get_list_characters_page():
    characters = []

    url = "https://rickandmortyapi.com/api/character/?page=1"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    characters.extend(dict["results"])

    url = "https://rickandmortyapi.com/api/character/?page=2"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    characters.extend(dict["results"])

    return render_template("characters.html", characters=characters)

@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    location_url = dict["location"]["url"]
    location_response = urllib.request.urlopen(location_url) 
    location_data = location_response.read()
    location_dict = json.loads(location_data)

    episodes_info = []

    for epi_url in dict["episode"]:
        epi_response = urllib.request.urlopen(epi_url)
        epi_data = epi_response.read()
        epi_dict = json.loads(epi_data)
        episodes_info.append(epi_dict)

    return render_template("profile.html", profile=dict, episodes=episodes_info, location=location_dict)

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
        "episode": character["episode.name"]
        }
        characters.append(character)

    return {"characters": characters}
    

@app.route("/locations")
def get_locations():

    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)
    locations = response.read()
    dict = json.loads(locations)

    return render_template("locations.html", locations=dict["results"])  


@app.route("/location/<id>")
def get_location(id):
    location_url = "https://rickandmortyapi.com/api/location/" + id
    location_response = urllib.request.urlopen(location_url) 
    location_data = location_response.read()
    location_dict = json.loads(location_data)

    characters_info = []

    for char_url in location_dict.get("residents", []):
        char_response = urllib.request.urlopen(char_url)
        char_data = char_response.read()
        char_dict = json.loads(char_data)
        characters_info.append(char_dict)

    return render_template("location.html", location=location_dict, characters=characters_info)

@app.route("/episodes")
def get_episodes():

    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    episodes = response.read()
    dict = json.loads(episodes)

    return render_template("episodes.html", episodes=dict["results"])      

@app.route("/episode/<id>")
def get_episode(id):
    epi_url = "https://rickandmortyapi.com/api/episode/" + id
    epi_response = urllib.request.urlopen(epi_url)
    epi_data = epi_response.read()
    epi_dict = json.loads(epi_data)

    characters_info = []

    for char_url in epi_dict["characters"]:
        char_response = urllib.request.urlopen(char_url)
        char_data = char_response.read()
        char_dict = json.loads(char_data)
        characters_info.append(char_dict)
        
    return render_template("episode.html", episode=epi_dict, characters=characters_info)