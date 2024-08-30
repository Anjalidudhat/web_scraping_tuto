from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.chrome()
driver.get("https://www.goibibo.com/hotels-international/ramada-by-wyndham-bali-sunset-road-kuta-hotel-in-bali-2607492164247448927/?hquery={%22ci%22:%2220240829%22,%22co%22:%2220240830%22,%22r%22:%221-2-0%22,%22ibp%22:%22%22}&cc=IDN&reviewType=gi&vcid=531325520167232868&locusId=CTBAL9d5bd6c3&locusType=city&cityCode=CTBAL9d5bd6c3")

driver.implicitly_wait(10)

hotel_name = driver.find_element(By.TAG_NAME, "h1").text
print("Hotel Name:", hotel_name)

driver.quit()