import requests
import lxml
from bs4 import BeautifulSoup

session = requests.Session()
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

url = f"https://cash-backer.club/shops?page = {j}"
for j in range(7):
    session = requests.Session()
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
    response = session.get(url, headers=header)
    soup = BeautifulSoup(response.text, "lxml")
    shops = soup.find("div", class_ ="shop-title")



