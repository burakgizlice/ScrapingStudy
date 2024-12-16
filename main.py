"""Main script of my application"""
import requests

response = requests.get("https://en.wikipedia.org/wiki/Khabib_Nurmagomedov")

with open("result.html", "w", encoding="utf-8") as f:
    f.write(response.text)