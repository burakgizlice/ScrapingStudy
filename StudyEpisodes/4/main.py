"""Getting the opponents and the outcome utilizing the Parsel library with
XPaths"""
from xpath_opponents import get_opponents
import requests
import json

response = requests.get("https://en.wikipedia.org/wiki/Dustin_Poirier")
print(response.status_code)

opponents_json = json.dumps(get_opponents(response.text))

with open("opponents.json", "w", encoding="utf-8") as f:
    f.write(opponents_json)
