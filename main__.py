import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == '__main__':
    email = "#"
    password = "#"

    options = webdriver.ChromeOptions()
    #options.add_argument('proxy-server=106.122.8.54:3128')
    options.add_argument(r'--user-data-dir=C:\Users\Skyne\AppData\Local\Google\Chrome\User Data\Default')

    browser = uc.Chrome(
        options=options,
        use_subprocess=True,
    )
    browser.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    # browser.get('https://nb-bet.com/')

    time.sleep(35)

    browser.find_element(By.ID, 'identifierId').send_keys(email)

    browser.find_element(
        By.CSS_SELECTOR, '#identifierNext > div > button > span').click()

    password_selector = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, password_selector)))

    browser.find_element(
        By.CSS_SELECTOR, password_selector).send_keys(password)

    browser.find_element(
        By.CSS_SELECTOR, '#passwordNext > div > button > span').click()