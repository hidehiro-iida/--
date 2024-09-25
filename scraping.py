import requests
from bs4 import BeautifulSoup

response = requests.get('https://zukan.pokemon.co.jp/')
# response = requests.get('https://narito.ninja/scraping.html')

# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

for h1 in soup.find_all('h2'):
    print("⭐️⭐️"+h1.text)