from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()                                             # three lines of code at 15,16 and 17 do same thing but output error messages.
options.add_experimental_option('excludeSwitches', ['enable-logging'])          # lines 10,11,12 stop that! Nicer log of data in terminal!

driver = webdriver.Chrome(options=options)
driver.get("https://www.agencycentral.co.uk/agencysearch/engineering/agencysearch.htm")

#chromedriver = 'C:/Users/James Mills/Documents/GitHub/Web Scraping/chromedriver.exe'       # finds chrome driver, assigns file path to variable
#driver = webdriver.Chrome(chromedriver)                                                    # use module webdriver to enable chromedriver.exe
#driver.get("https://www.google.com/")                                                      # opens URL associated to .get function

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
    

def all_other_agencies():                                           # placeholder for additional function to access rest of the URL's on this page.
    i = 0


first_agency()

time.sleep(30)                                                                               # keeps tab open for 20 seconds
driver.quit()                                                                               # closes window, ends program

