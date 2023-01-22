from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pickle
import requests

options = webdriver.ChromeOptions()                                                         # three lines of code at 15,16 and 17 do same thing but output error messages.
options.add_experimental_option('excludeSwitches', ['enable-logging'])                      # lines 10,11,12 stop that! Nicer log of data in terminal!

driver = webdriver.Chrome(options=options)
driver.get("https://www.agencycentral.co.uk/agencysearch/engineering/agencysearch.htm")

cookies = pickle.load(open('cookies.pkl', 'rb'))
for cookie in cookies:
    driver.add_cookie(cookie)

elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="contact-button-visit-website"]')))

for element in elements:
    print(element.text)
    print(element.get_attribute('outerHTML'))


time.sleep(500)
