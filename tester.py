# from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

s = Service('C:\\Users\\Skyne\\PycharmProjects\\NewProject\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("https://www.github.com")
# driver.implicitly_wait(10)
time.sleep(5)
search = driver.find_element(By.ID, 'user_email')
# 8UrHYfhK3u@8Fxf
# skynet-bl@gmail.com   alexsey_com@mail.ru Jekobs
search.send_keys('roman@examle.com')
search.send_keys(Keys.RETURN)

# driver.implicitly_wait(10)
time.sleep(10)
print(driver.title)
