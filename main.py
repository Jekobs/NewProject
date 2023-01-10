import undetected_chromedriver as uc
import time
options = uc.ChromeOptions()

# setting profile
options.user_data_dir = "c:\\temp\\profile"

# use specific (older) version
driver = uc.Chrome(options=options, version_main=94)  # version_main allows to specify your chrome version instead of following chrome global version

driver.get('https://nowsecure.nl')   # my own test test site with max anti-bot protection
ta