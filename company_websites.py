######
# function: opens up website for agency central and crawls through to the 1st recruitment agency website.
# future improvements:
#   - use of cookies instead of the function "first_agency" to minimise time spent running program on startup.
#   - "first_agency_xpaths" file will change from full xpath to xpath relative to features on page, will improve redundancy if website is updated in future.
#   - collect url once individual agency website reached, close tab, repeat for entire page.
#   - click on next page once all data for current agencies on page is collected.
#   - upload data into excel alongside the "company_name" script.
######


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromedriver = 'C:/Users/James Mills/Documents/GitHub/Web Scraping/chromedriver.exe'       # finds chrome driver, assigns file path to variable
driver = webdriver.Chrome(chromedriver)                                                    # use module webdriver to enable chromedriver.exe
driver.get("https://www.agencycentral.co.uk/agencysearch/engineering/agencysearch.htm")    # opens URL associated to .get function

filePath1 = r"C:\Users\James Mills\Documents\GitHub\Web-Scraping-Scripts\first_agency_xpaths.txt"
openFile1 = open(filePath1,"r")
data1 = openFile1.read()
xpaths = data1.split("\n")

filePath2 = r"C:\Users\James Mills\Documents\GitHub\Web-Scraping-Scripts\first_agency_actions.txt"
openFile2 = open(filePath2,"r")
data2 = openFile2.read()
steps = data2.split("\n")

def first_agency():
    c = -1
    for step in steps:
        if step == "click()":
            c = c + 1
            time.sleep(2)
            clickable = driver.find_element(By.XPATH, xpaths[c]).click()
        elif step != "click()":
            time.sleep(2)
            infoEnter = driver.find_element(By.XPATH, xpaths[c]).send_keys(step)
    

def all_other_agencies():                                                                   # placeholder for additional function to access rest of the URL's on this page.
    i = 0

first_agency()

time.sleep(30)                                                                              # keeps tab open for 20 seconds
driver.quit()                                                                               # closes window, ends program

