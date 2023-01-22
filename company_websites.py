######
# function: opens up website for agency central and crawls through to the 1st recruitment agency website.
# future improvements:
#   - click on next page once all data for current agencies on page is collected
#   - upload data into excel alongside the "company_name" script
######

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time

url_list = []                                                                                           # blank list to contain all collected URL's. Will be added to excel at a later stage.
branch_list = []

filePath = r"C:\Users\James Mills\Documents\GitHub\Web-Scraping-Scripts\uk_cities_listed.txt"           # angency central requires some locational input for certain agencies, this code accesses a list of cities in UK for reference where required.
openFile = open(filePath,"r")
data = openFile.read()
cities = data.split("\n")

options = webdriver.ChromeOptions()                                                                     # allows for use of ChromeDriver without exceptions flagging up or other bugs that are yet to be removed.
options.add_experimental_option('excludeSwitches', ['enable-logging'])                      
driver = webdriver.Chrome(options=options)
driver.get("https://www.agencycentral.co.uk/agencysearch/engineering/agencysearch.htm")

cookies = pickle.load(open('cookies.pkl', 'rb'))                                                        # loads cookies to the browser
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()                                                                                        # refresh page to implement cookies loaded previously
elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="contact-button-visit-website"]')))        # collects all relevant elemants by rel. XPATH.

def location():
    time.sleep(5)                                                                                       # needs a manual wait for driver to update with current tab('window') count
    if len(driver.window_handles) == 1:
        try:
            WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="agency-branch-selection"]/div[3]/div/ul/li/span[1]'))).click()        
        finally:
            pass
    else:
        pass 


def agency_url():                                                                                        # function to iterate through the data collected by "elements".                                                                                     # limits loop, will remove once script ready to go through entire website.
        for element in elements:                                                                         # for each instance of data collected in the list "elements"...        
            element.click()                                                                              # click on the relvant element  
            location()                                                                                   # runs function "location"                           
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))                               # driver waits for number of tabs to = 2 before moving onto next operation
            new_tab = driver.window_handles[1]                                                           # window handles is a list of the various tabs open in a browser
            driver.switch_to.window(new_tab)                                                             # switches focus to new tab
            url_collect = driver.current_url                                                             # collects current tab's URL
            print(url_collect)                                                                           # for reference
            url_list.append(url_collect)                                                                 # appends collected URL data to list "url_list"
            driver.close()                                                                               # closes current tab
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(1))                               # waits for driver to see total number of tabs = 1
            driver.switch_to.window(driver.window_handles[0])                                            # focuses on orignal tab
            time.sleep(3)

agency_url()
    
time.sleep(5)                                                                                            # keeps tab open for 5 seconds
driver.quit()                                                                                            # closes window, ends program

