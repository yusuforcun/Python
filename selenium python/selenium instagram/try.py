
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

tarayıcı=webdriver.Firefox()

tarayıcı.get("https://www.instagram.com/accounts/login/")
print("tarayıcı acıldı")
time.sleep(1) 

button=tarayıcı.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button/div")
print("girildi")
time.sleep(10)