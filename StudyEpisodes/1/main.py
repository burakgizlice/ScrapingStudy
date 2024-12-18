"""Setting up the environment, and learning about how to work with requests."""
import requests

response = requests.get("https://en.wikipedia.org/wiki/Khabib_Nurmagomedov")

with open("result.html", "w", encoding="utf-8") as f:
    f.write(response.text)