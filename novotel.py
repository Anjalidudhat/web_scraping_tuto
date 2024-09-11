# from selenium import webdriver
# from bs4 import BeautifulSoup
# import requests

# url = "https://www.goibibo.com/hotels-international/novotel-paris-centre-tour-eiffel-hotel-in-paris-1585977246363947094/?"

# r = requests.get(url)

# soup = BeautifulSoup(r.text, "html.parser")

# hotel_name = soup.find(class_="HotelInfostyles__CenterDiv-sc-138dfbx-0 dWAtPb").get_text(strip=True)

# print(hotel_name)






from selenium import webdriver
from bs4 import BeautifulSoup
import json

driver = webdriver.Chrome()

url = "https://www.goibibo.com/hotels/sheraton-grand-bengaluru-whitefield-convention-centre-hotel-in-bangalore-3133239078443520360/?"
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")

hotel_name = soup.find("h1", class_="dwebCommonstyles__SectionHeaderSEO-sc-112ty3f-7 HotelName__HotelNameText-sc-1o26jsk-0 iPuYcF kKFHdD")
if hotel_name:
    hotel_name = hotel_name.get_text(strip=True)
else:
    hotel_name = "Hotel name is not define"

hotel_karnatka = soup.find(class_="HotelAddressText__HotelCompleteAddressSpan-sc-1lcrowf-4 ksRwiT")
if hotel_karnatka:
    hotel_karnatka = hotel_karnatka.get_text(strip=True)
else:
    hotel_karnatka = "In hotel not available in hoodi"

hotel_about = soup.find(class_="PropertyHighlightsstyles__PropertyHighlightsBody-sc-n1nlv6-3 PrLSK")
if hotel_about:
    hotel_about = hotel_about.get_text(strip=True)
else:
    hotel_about = "Not available several types of varities"

hotel_twin = soup.find(class_="ElitePackageCardstyles__ContentWrapper-sc-17rrd4u-6 bGfBrH")
if hotel_twin:
    hotel_twin = hotel_twin.get_text(strip=True)
else:
    hotel_twin = "Not available bathroom"

hotel_room = soup.find(class_="RoomFlavorstyles__RoomFlavorColumn-sc-90vv8b-0 ihNAES")
if hotel_room:
    hotel_room = hotel_room.get_text(strip=True)
else:
    hotel_room = "Room are not available"

hotel_spa = soup.find(class_="Amenitiesstyles__CategorizedAmenitiesTableContainer-sc-e2msby-11 dgHjeh")
if hotel_spa:
    hotel_spa = hotel_spa.get_text(strip=True)
else:
    hotel_spa = "Facilities not available"

hotel_food = soup.find(class_="DiningDetailsUIstyles__DiningWrapper-sc-qu13qq-0 eTmcHX")
if hotel_food:
    hotel_food = hotel_food.get_text(strip=True)
else:
    hotel_food = "Food are not available"

hotel_reviews = soup.find(class_="Layouts__Column-sc-1yzlivq-1 UserReviewstyles__UserReviewOuterWrapperDiv-sc-uxnwyv-2 kWbCjO bvbaMk")
if hotel_reviews:
    hotel_reviews = hotel_reviews.get_text(strip=True)
else:
    hotel_reviews = "It's very poor"

hotel_property = soup.find(class_="dwebCommonstyles__BaseColumnWrap-sc-112ty3f-2 hclYdS")
if hotel_property:
    hotel_property = hotel_property.get_text(strip=True)
else:
    hotel_property = "Hotel property is destory"


print(hotel_name)
print(hotel_karnatka)
print(hotel_about)
print(hotel_twin)
print(hotel_room)
print(hotel_spa)
print(hotel_food)
print(hotel_reviews)
print(hotel_property)


hotel_data = {
    "hotel_name": hotel_name,        # Use colon instead of equal sign
    "hotel_karnatka": hotel_karnatka,
    "hotel_about": hotel_about,
    "hotel_twin": hotel_twin,
    "hotel_room": hotel_room,
    "hotel_spa": hotel_spa,
    "hotel_food": hotel_food,
    "hotel_reviews": hotel_reviews,
    "hotel_property": hotel_property
}

hotel_data_json = json.dumps(hotel_data, indent=4)

print(hotel_data_json)




# from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Setup Selenium WebDriver
# driver = webdriver.Chrome()

# # URL of the hotel page
# url = "https://www.goibibo.com/hotels-international/novotel-paris-centre-tour-eiffel-hotel-in-paris-1585977246363947094/?"
# driver.get(url)

# # Wait for the hotel name to load (dynamic content)
# try:
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "HotelName__HotelNameText-sc-1o26jsk-0"))
#     )
# except Exception as e:
#     print("Error waiting for hotel name to load:", e)

# # Parse the page source
# soup = BeautifulSoup(driver.page_source, "html.parser")

# # Try to find the hotel name
# hotel_name = soup.find("h2", class_="HotelName__HotelNameText-sc-1o26jsk-0")
# if hotel_name:
#     hotel_name = hotel_name.get_text(strip=True)
# else:
#     hotel_name = "Hotel name is not defined"

# # Print the hotel name
# print(hotel_name)

# # Close the browser
# driver.quit()
