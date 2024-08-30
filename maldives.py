# from bs4 import BeautifulSoup
# import requests


# url = "https://www.goibibo.com/hotels-international/coco-palm-dhuni-kolhu-maldives-hotel-in-maldives-2122491043573729579/?"

# r = requests.get(url)

# soup = BeautifulSoup(r.text,"html.parser")

# hotel_name = soup.find("h2", class_="dwebCommonstyles__SectionHeaderSEO-sc-112ty3f-7 HotelName__HotelNameText-sc-1o26jsk-0 HdCjY jiRwRm").get_text(strip=True)

# print(hotel_name)

from bs4 import BeautifulSoup
import requests

url = "https://www.goibibo.com/hotels-international/coco-palm-dhuni-kolhu-maldives-hotel-in-maldives-2122491043573729579/?"

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

# Try to find the hotel name with a more general approach
hotel_name_element = soup.find("h2")
hotel_name = hotel_name_element.get_text(strip=True) if hotel_name_element else "Hotel name not found"

print(hotel_name)
