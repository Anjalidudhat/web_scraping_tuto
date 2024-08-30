# from bs4 import BeautifulSoup
# import requests

# url = "https://in.hotels.com/ho151699/taj-palace-new-delhi-new-delhi-india/?chkin=2024-09-12&chkout=2024-09-14&x_pwa=1&rfrr=HSR&pwa_ts=1724899554972"

# r = requests.get(url)

# soup = BeautifulSoup(r.text, "html.parser")

# hotel_name = soup.find("h1", class_="uitk-heading uitk-heading-3").get_text(strip=True)

# print(hotel_name)


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode for faster performance
# service = Service('/path/to/chromedriver')  # Replace with the path to your chromedriver

# driver = webdriver.Chrome(service=service, options=chrome_options)
# driver.get(url)

# hotel_name = driver.find_element(By.TAG_NAME, "h1").text
# print(hotel_name)

# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# # Set up Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode for scraping

# # Set up the WebDriver (make sure you have the correct path to your ChromeDriver)
# service = Service('/media/anjali/44364716364707FE/learning/webscraping/chromedriver')  # Replace with the path to your ChromeDriver
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Open the URL
# driver.get("https://www.booking.com/hotel/in/nirvana-hill-resort.en-gb.html")

# # Find the hotel name element
# hotel_name_element = driver.find_element(By.CLASS_NAME, "pp-header__title")
# hotel_name = hotel_name_element.text

# hotel_address_element = driver.find_element(By.CLASS_NAME, "hp_address_subtitle js-hp_address_subtitle jq_tooltip")
# hotel_address = hotel_name_element.text


# # Print the hotel name
# print(hotel_name)
# print(hotel_address)

# # Close the WebDriver
# driver.quit()




# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Set up Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode for scraping

# # Set up the WebDriver (make sure you have the correct path to your ChromeDriver)
# service = Service('/media/anjali/44364716364707FE/learning/webscraping/chromedriver')  # Replace with the path to your ChromeDriver
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Open the URL
# driver.get("https://www.booking.com/hotel/in/nirvana-hill-resort.en-gb.html")

# # Wait for the hotel name element to be present
# hotel_name_element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "pp-header__title"))
# )
# hotel_name = hotel_name_element.text

# # Wait for the hotel address element to be present
# hotel_address_element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "hp_address_subtitle"))
# )
# hotel_address = hotel_address_element.text

# # Wait for the hotel garden element (using CSS Selector as a more robust method)
# try:
#     hotel_garden_element = WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".hprt-block"))
#     )
#     hotel_garden = hotel_garden_element.text
#     print(hotel_garden)
# except TimeoutException:
#     print("The hotel garden element could not be found or took too long to load.")

# # Print the hotel name and address
# print(hotel_name)
# print(hotel_address)

# # Close the WebDriver
# driver.quit()



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Import TimeoutException

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode for scraping

# Set up the WebDriver (make sure you have the correct path to your ChromeDriver)
service = Service('/media/anjali/44364716364707FE/learning/webscraping/chromedriver')  # Replace with the path to your ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the URL
driver.get("https://www.booking.com/hotel/in/nirvana-hill-resort.en-gb.html")

# Wait for the hotel name element to be present
hotel_name_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "pp-header__title"))
)
hotel_name = hotel_name_element.text

# Wait for the hotel address element to be present
hotel_address_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "hp_address_subtitle"))
)
hotel_address = hotel_address_element.text

# Wait for the hotel garden element (using CSS Selector as a more robust method)
try:
    hotel_garden_element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".hprt-block"))
    )
    hotel_garden = hotel_garden_element.text
    print(hotel_garden)
except TimeoutException:
    print("The hotel garden element could not be found or took too long to load.")

# Print the hotel name and address
print(hotel_name)
print(hotel_address)

# Close the WebDriver
driver.quit()

