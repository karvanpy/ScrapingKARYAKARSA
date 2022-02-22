# Scrape KARYAKARSA

# import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url = "https://karyakarsa.com/discover"

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get(url)

content = driver.page_source

soup = BeautifulSoup(content, "html.parser")

kreator_minggu_ini = []

discover = soup.find_all("a", {"class": "q-item q-item-type row no-wrap q-py-md q-mb-md postbox bordered top-weekly-item q-item--clickable q-link cursor-pointer q-focusable q-hoverable"})
for kreator in discover:
	kreator_minggu_ini.append({
		"urutan": kreator.find("big", {"class": "text-center text-weight-bold text-white"}).text,
		"username": kreator.find("div", {"class": "q-item__label text-white text-weight-bold"}).text,
		"kategori": kreator.find("div", {"class": "q-item__label text-white q-item__label--caption text-caption"}).text
		})

print(json.dumps(kreator_minggu_ini, indent=4))
driver.close()