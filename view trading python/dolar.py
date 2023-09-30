import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

op=webdriver.Chrome();
options = Options()
options.add_argument('--headless')
op.get("https://tr.tradingview.com/symbols/USDTRY/?exchange=FX")

dolar = op.find_element(By.XPATH,"//*[@id='anchor-page-1']/div/div[3]/div[1]/div/div/div/div[1]/div[1]")
print(dolar)