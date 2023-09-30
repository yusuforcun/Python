from selenium import webdriver
import time
from selenium.webdriver.common.by import By

tarayıcı=webdriver.Firefox()

tarayıcı.get("https://www.instagram.com/gencbizz/following/")
print("tarayıcı acıldı")
time.sleep(1) 

button=tarayıcı.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[8]/div[2]/div[1]/div/div/div/span/a/span/div")
print("button")
time.sleep(10)