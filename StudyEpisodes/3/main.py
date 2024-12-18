"""Learning to maneuver between different strategies, also working with CSS
Selectors."""
import requests
import json
# from bs_opponents import get_opponents
from bs_select_opponent import get_opponents

response = requests.get("https://en.wikipedia.org/wiki/Khabib_Nurmagomedov")
print(response.status_code)

opponents = get_opponents(response.text)
opponents_json = json.dumps(opponents)

with open("opponents.json", "w", encoding="utf-8") as f:
    f.write(opponents_json)