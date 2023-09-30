from selenium import webdriver
import time
from selenium.webdriver.common.by import By

tarayıcı=webdriver.Firefox()

tarayıcı.get("https://www.instagram.com/accounts/login/")
print("tarayıcı acıldı")
time.sleep(1)

username=tarayıcı.find_element(By.NAME,"username")
password=tarayıcı.find_element(By.NAME,"password")

username.send_keys("yusufufus")
password.send_keys("27982798Yo.")

loginbutton=tarayıcı.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button/div")
loginbutton.click()
time.sleep(5)




bilgikaydetme=tarayıcı.find_element(By.CSS_SELECTOR,"#mount_0_0_Wt > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > section > nav > div._acc1._acc3 > div > div > div._acuq._acur > div > div:nth-child(1) > div > a > svg")
bilgikaydetme.click()
print("bilgi kaydetti")
time.sleep(1)

bilgi=tarayıcı.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button/div")
loginbutton.click()
bilgi.click()

# tr2=tarayıcı.find_element(By.XPATH,"//*[@id='mount_0_0_fF'']/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
# tr2.click()
# time.sleep(1)

# try3=tarayıcı.find_element(By.XPATH,"//*[@id='mount_0_0_wz']/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
# try3.click()


time.sleep(1000)