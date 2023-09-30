from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser=webdriver.Firefox()

browser.get("https://twitter.com/i/flow/login")
time.sleep(1)
print("twitter açıldı")

# anlamadıgım nedenlerle çalışmıyor

username=browser.find_element(By.XPATH,("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"))

loginbutton=browser.find_element(By.XPATH,("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span"))


username.send_keys("yusufufuss")
print("kullanıcı adı  girildi")
time.sleep(1)

# password=browser.find_element(By.XPATH,("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"))

# passwordbutton=browser.find_element(By.XPATH,("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span"))

loginbutton.click()
print("password page  opened ")
time.sleep(1)

# password.send_keys("27982798Yo.")
# time.sleep(1)
# print("şifre yazıldı")


# passwordbutton.click()
# print("clicklendi")
# time.sleep(5)