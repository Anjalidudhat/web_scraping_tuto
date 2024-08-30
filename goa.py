

from bs4 import BeautifulSoup
import requests
import json

url = "https://www.booking.com/hotel/in/holiday-inn-goa-candolim.en-gb.html?"

r = requests.get(url)

# Corrected the parser name to "html.parser"
soup = BeautifulSoup(r.text, "html.parser")

hotel_name = soup.find("h2", class_="af32860db5 pp-header__title").get_text(strip=True)
hotel_address = soup.find(class_="hp_address_subtitle js-hp_address_subtitle jq_tooltip").get_text(strip=True)
hotel_get = soup.find(class_="e2585683de c8d1788c8c").get_text(strip=True)
hotel_king = soup.find(class_="eb73dc0c10 eb02592978 ad0b39688b").get_text(strip=True)



print(hotel_name)
print(hotel_address)
print(hotel_get)
print(hotel_king)

