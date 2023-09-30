import time

from selenium.webdriver.common.by import By
from selenium import webdriver 

driver=webdriver.Firefox()
 
url="https://eksisozluk.com/mustafa-kemal-ataturk--34712"

driver.get(url)


elements = driver.find_elements(By.CSS_SELECTOR, ".content")


for elemen in elements :
    print(elemen.text)

driver.close()
