from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Google hesap bilgilerinizi buraya girin
username = "orcun8522@gmail.com"
password = "27982798Yo."

# Google oturum açma sayfasının URL'si  
login_url = "https://accounts.google.com/signin/v2/identifier"

# WebDriver'ı başlatın ve oturum açma sayfasını açın
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(login_url)
time.sleep(3)

# Kullanıcı adını girin ve "İleri" düğmesine tıklayın
email_input = driver.find_element_by_xpath('//*[@id="identifierId"]')
email_input.send_keys(username)
email_input.send_keys(Keys.RETURN)
time.sleep(3)

# Şifreyi girin ve "İleri" düğmesine tıklayın
password_input = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)
time.sleep(5)

# Google Ana Sayfasını açın
google_url = "https://www.google.com.tr"
driver.get(google_url)