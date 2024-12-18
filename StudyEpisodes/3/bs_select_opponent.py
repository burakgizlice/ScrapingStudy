"""A Function for applying logic to pull opponents data from the wiki page"""
from bs4 import BeautifulSoup
def get_opponents(html):
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.title.string)

    tables = soup.select('table[class="wikitable"]')
    matches = tables[0]
    trs = matches.select("tr")

    opponents = []
    for tr in trs:
        opponent = {}
        opponent_node = tr.select_one("td:nth-child(3)")

        if not opponent_node:
            continue

        opponent_name = opponent_node.string
        opponent_url = ""

        if opponent_name is None:
            a_tag = opponent_node.select_one("a")
            opponent_name = a_tag.string
            opponent_url = "https://en.wikipedia.org" + a_tag["href"]

        opponent["name"] = opponent_name.strip('\n')
        opponent["URL"] = opponent_url
        opponents.append(opponent)
    return opponents