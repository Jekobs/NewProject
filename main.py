#Importing Necessary Libraries
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as webdriver
import time

#bypass function
def seleniumUndetected():
    # options = webdriver.ChromeOptions()
    # # profile = "C:\\Users\\Skyne\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
    # options.add_argument('user-data-dir=C:\\Users\\Skyne\\AppData\\Local\\Google\\Chrome\\User Data')
    # options.add_argument('profile-directory=Default')
    # driver = webdriver.Chrome(options=options,use_subprocess=True)
    #
    #
    # driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    # # driver.get("https://nb-bet.com/")
    # # driver.implicitly_wait(10)
    # time.sleep(35)

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
    time.sleep(20)

#driver
if __name__ == "__main__":
    seleniumUndetected() #call the function
