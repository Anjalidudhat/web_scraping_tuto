# from bs4 import BeautifulSoup
# import requests

# url = "https://www.goibibo.com/hotels/the-ananta-hotel-in-udaipur-3092563685294070315/?"

# r = requests.get(url)

# soup = BeautifulSoup(r.text, "html.parser")

# hotel_name = soup.find("h2", class_="dwebCommonstyles__SectionHeaderSEO-sc-112ty3f-7 HotelName__HotelNameText-sc-1o26jsk-0 iPuYcF kKFHdD").get_text(strip=True)

# hotel_address = soup.find(class_="HotelAddressText__HotelCompleteAddressSpan-sc-1lcrowf-4 ksRwiI").get_text(strip=True)

# print(hotel_name)
# print(hotel_address)


# from bs4 import BeautifulSoup
# import requests

# url = "https://www.goibibo.com/hotels/the-ananta-hotel-in-udaipur-3092563685294070315/?"

# r = requests.get(url)

# soup = BeautifulSoup(r.text, "html.parser")

# # Try a more general tag search for the hotel name
# hotel_name = soup.find("h2")
# if hotel_name:
#     hotel_name = hotel_name.get_text(strip=True)
# else:
#     hotel_name = "Hotel name not found"

# # Try finding the address in a simpler way
# hotel_address = soup.find("span", class_="HotelAddressText__HotelCompleteAddressSpan-sc-1lcrowf-4 ksRwiI")
# if hotel_address:
#     hotel_address = hotel_address.get_text(strip=True)
# else:
#     hotel_address = "Hotel address not found"

# print(hotel_name)
# print(hotel_address)


from selenium import webdriver
from bs4 import BeautifulSoup

# Set up your browser driver
driver = webdriver.Chrome()  # You need to download and set up the appropriate driver for your browser

url = "https://www.goibibo.com/hotels/the-ananta-hotel-in-udaipur-3092563685294070315/?"
driver.get(url)

# After the page is loaded, extract the HTML
soup = BeautifulSoup(driver.page_source, "html.parser")

# Proceed with scraping as before
hotel_name = soup.find("h2")
if hotel_name:
    hotel_name = hotel_name.get_text(strip=True)
else:
    hotel_name = "Hotel name not found"

hotel_address = soup.find("span", class_="HotelAddressText__HotelCompleteAddressSpan-sc-1lcrowf-4 ksRwiI")
if hotel_address:
    hotel_address = hotel_address.get_text(strip=True)
else:
    hotel_address = "Hotel address not found"

hotel_room = soup.find(class_="RoomFlavorstyles__RoomFlavorColumn-sc-90vv8b-0 ihNAES")
if hotel_room:
    hotel_room = hotel_room.get_text(strip=True)
else:
    hotel_room = "Hotel rooms are not found"

hotel_food = soup.find(class_="dwebCommonstyles__BaseColumnWrap-sc-112ty3f-2 MultiRestaurentUIstyles__ContentWrap-sc-l9oz98-2 hclYdS jAcNb")
if hotel_food:
    hotel_food = hotel_food.get_text(strip=True)
else:
    hotel_food = "food is not available"

hotel_reviews = soup.find(class_="Layouts__Row-sc-1yzlivq-0 RatingsBreakupstyles__WrapperDiv-sc-1w4l82j-0 hbwzEv fXaVwh")
if hotel_reviews:
    hotel_reviews = hotel_reviews.get_text(strip=True)
else:
    hotel_reviews = "Not available"

hotel_reviews2 = soup.find(class_="Layouts__Row-sc-1yzlivq-0 UserReviewstyles__UserDetailsAndRatingWrapperDiv-sc-uxnwyv-5 hbwzEv Pvelq")
if hotel_reviews2:
    hotel_reviews2 = hotel_reviews2.get_text(strip=True)
else:
    hotel_reviews2 = "Not found"

hotel_policy = soup.find(class_="Policystyles__PolicyHeaderStyled-sc-1c9fldk-1 jtjiWc")
if hotel_policy:
    hotel_policy = hotel_policy.get_text(strip=True)
else:
    hotel_policy = "policy are not define"

hotel_passport = soup.find(class_="dwebCommonstyles__BaseColumnWrap-sc-112ty3f-2 hclYdS")
if hotel_passport:
    hotel_passport = hotel_passport.get_text(strip=True)
else:
    hotel_passport = "passport are not necessar"


hotel_hi = soup.find(class_="UserAnswerstyles__QuestionTextWrapper-sc-1c5jue4-5 cKSNUj")
if hotel_hi:
    hotel_hi = hotel_hi.get_text(strip=True)
else:
    hotel_hi = "Hotel closed"

hotel_air = soup.find(class_="SimilarHotelAmenitiesstyles__HotelAmenitiesWrapOuterDiv-sc-lv7ss5-0 fEtXIP")
if hotel_air:
    hotel_air = hotel_air.get_text(strip=True)
else:
    hotel_air = "air condition free"

print(hotel_name)
print(hotel_address)
print(hotel_room)
print(hotel_food)
print(hotel_reviews)
print(hotel_reviews2)
print(hotel_policy)
print(hotel_passport)
print(hotel_hi)
print(hotel_air)

# Don't forget to close the browser
driver.quit()
