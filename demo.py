from bs4 import BeautifulSoup
import requests
import json

url = "https://www.booking.com/hotel/in/nirvana-hill-resort.en-gb.html?"

r = requests.get(url)

soup = BeautifulSoup(r.text,"html.parser")

hotel_name = soup.find("h2",class_="af32860db5 pp-header__title").get_text(strip=True)
hotel_address = soup.find("span",class_="hp_address_subtitle js-hp_address_subtitle jq_tooltip").get_text(strip=True)
hotel_description = soup.find(class_="hp_desc_main_content").get_text(strip=True)
hotel_facilities = soup.find(class_="eb73dc0c10 eb02592978 ad0b39688b").get_text(strip=True)
hotel_outdoor = soup.find("ul", class_="b3605c5e50 eb11e518ca bdfadf615e").get_text(strip=True)
hotel_fine = soup.find(class_="d3c6350bdd eb02592978 ad0b39688b").get_text(strip=True)
hotel_need = soup.find(class_="e64db3afd5 ab107395cb f11fd93660").get_text(strip=True)    
print(hotel_name)
print(hotel_address)
print(hotel_description)
print(hotel_facilities)
print(hotel_outdoor)
print(hotel_fine)
print(hotel_need)


hotel_data = {
    "hotel_name": hotel_name,
    "hotel_address": hotel_address,
    "hotel_description": hotel_description,
    "hotel_facilities": hotel_description,
    "hotel_outdoor": hotel_outdoor,
    "hotel_fine": hotel_fine,
    "hotel_need": hotel_need
}

hotel_data_json = json.dumps(hotel_data, indent=4)

print(hotel_data_json)
