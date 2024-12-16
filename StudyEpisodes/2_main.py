"""Getting the opponents in a table for Khabib's wikipedia page"""
import requests
from bs4 import BeautifulSoup
import json

response = requests.get("https://en.wikipedia.org/wiki/Khabib_Nurmagomedov")
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.string)

tables = soup.find_all("table", attrs={"class": "wikitable"})
matches = tables[1]
trs = matches.find_all("tr")

opponents = []
for tr in trs:
    tds = tr.find_all("td")

    if not tds:
        continue

    opponent_node = tds[2]
    opponent_name = opponent_node.string

    if opponent_name is None:
        opponent_name = opponent_node.a.string

    opponents.append(opponent_name.strip('\n'))

opponents_json = json.dumps(opponents)

with open('StudyEpisodes/opponents.json', 'w', encoding="utf-8") as f:
    f.write(opponents_json)
