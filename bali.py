import requests
from bs4 import BeautifulSoup

url = "https://www.goibibo.com/hotels-international/ramada-by-wyndham-bali-sunset-road-kuta-hotel-in-bali-2607492164247448927/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

# Try a more general approach
hotel_name = soup.find("h1")
if hotel_name:
    print(hotel_name.get_text(strip=True))
else:
    print("Hotel name not found.")
