import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

browser=webdriver.Firefox()

url="https://eksisozluk.com/mustafa-kemal-ataturk--34712"

browser.get(url)

elements = browser.find_elements(By.CSS_SELECTOR, ".content")
# dosya = open("hitabe.txt", "w")

for element in elements :
    # dosya.write(elemen.text)
    print("***************")
    print(element.text)
    
    

# dosya.close()
browser.close()
