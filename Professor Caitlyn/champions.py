import requests
import json


champions = requests.get("http://ddragon.leagueoflegends.com/cdn/12.20.1/data/en_US/champion.json")
champions = champions.json()
with open("championslist.json", "w") as outfile:
    json.dump(champions, outfile, indent=1)