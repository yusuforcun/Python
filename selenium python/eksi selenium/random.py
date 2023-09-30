import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
 
url="https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="


entries=[]
entrycount=1

x=random.randint(1,2556)
for i in range(4):
    newUrl = url + str(x)
    driver.get(newUrl)
    elements=driver.find_elements(By.CSS_SELECTOR, ".content")
    for element in elements:
        entries.append(element.text)
        x=random.randint(1,2556)
    time.sleep(0.3)

for entry in entries :
    print(str(entrycount)+"**********************")
    print(element.text)
    entrycount+=1
     
driver.close()

