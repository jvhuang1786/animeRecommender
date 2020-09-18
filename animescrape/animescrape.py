import requests
import csv
from requests_html import HTML, HTMLSession

session = HTMLSession()
r = session.get('https://www.anime-planet.com/characters/all')

print(r.text)
