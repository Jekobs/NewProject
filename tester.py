# coding: utf8

# from selenium import webdriver

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup as BS
# import time
#
# s = Service('C:\\Users\\Skyne\\PycharmProjects\\NewProject\\chromedriver.exe')
# driver = webdriver.Chrome(service=s)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as BS
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path='C:\\Users\\Skyne\\PycharmProjects\\NewProject\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)
# driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
driver.get("https://nb-bet.com/")
# driver.implicitly_wait(10)
time.sleep(35)

search = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[1]/div/div[1]/div/div[3]/a[1]")
search.click()
time.sleep(3)

search2 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div[2]/div/form/div[1]/div[2]/input")
search2.send_keys('zagubastik@mail.ru')
search2.send_keys(Keys.RETURN)
search3 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div[2]/div/form/div[2]/div[2]/input")
search3.send_keys('stik_001')
search3.send_keys(Keys.RETURN)
search4 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div[2]/div/form/button")
search4.click()

# driver.implicitly_wait(10)
time.sleep(10)
# soup = BS(driver.page_source, 'html.parser')
with open("progects.html", "w", encoding="utf-8") as file:
    file.write(driver.page_source)
# print(driver.page_source)
driver.close()
