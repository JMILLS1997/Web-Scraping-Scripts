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

def first_agency():
    clickable = [
        "/html/body/div[2]/div/div[2]/section/div/section/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div/div[3]/div/div[1]/a",
        "/html/body/div[2]/div/div[2]/section/div/section/div/div/div[3]/div/div/div/div/div/div[2]/div/div/a",
        "/html/body/div[2]/div/div[2]/section/div/section/div/div/div[3]/div/div/div/div/div/div[1]/div[102]/div[1]/div[2]/section/div/div[4]/div/div[2]/span",
        "/html/body/div[2]/div/div[2]/section/div/section/div/div/div[3]/div/div/div/div/div/div[1]/div[102]/div[1]/div[2]/section/div/div[2]/div[2]/div[1]/div/form/div[1]/input",
        "/html/body/div[2]/div/div[2]/section/div/section/div/div/div[3]/div/div/div/div/div/div[1]/div[102]/div[1]/div[2]/section/div/div[2]/div[2]/div[1]/div/form/div[2]/input",
        "/html/body/div[2]/div/div[2]/section/div/section/div/div/div[3]/div/div/div/div/div/div[1]/div[102]/div[1]/div[2]/section/div/div[2]/div[2]/div[1]/div/form/div[3]/input",
        "/html/body/div[2]/div/div[2]/section/div/section/div/div/div[3]/div/div/div/div/div/div[1]/div[102]/div[1]/div[2]/section/div/div[2]/div[2]/div[1]/div/form/div[7]/input",
        "/html/body/div[2]/div/div[2]/section/div/section/div/div/div[3]/div/div/div/div/div/div[1]/div[102]/div[1]/div[2]/section/div/div[2]/div[2]/div[1]/div/form/div[8]/div/input",
        "/html/body/div[2]/div/div[2]/section/div/section/div/div/div[3]/div/div/div/div/div/div[1]/div[102]/div[1]/div[2]/section/div/div[2]/div[2]/div[1]/div/form/div[8]/div/input"
    ]

    driver.find_element(By.XPATH, clickable[0]).click()
    driver.find_element(By.XPATH, clickable[1]).click()
    time.sleep(2)
    driver.find_element(By.XPATH, clickable[2]).click()
    time.sleep(2)
    driver.find_element(By.XPATH, clickable[3]).click()
    driver.find_element(By.XPATH, clickable[3]).send_keys("Joe")
    driver.find_element(By.XPATH, clickable[4]).click()
    driver.find_element(By.XPATH, clickable[4]).send_keys("Blogs")
    driver.find_element(By.XPATH, clickable[5]).click()
    driver.find_element(By.XPATH, clickable[5]).send_keys("Engineer")
    driver.find_element(By.XPATH, clickable[6]).click()
    time.sleep(2)
    driver.find_element(By.XPATH, clickable[7]).click()
    time.sleep(2)
    
    

def all_other_agencies():                                           # placeholder for additional function to access rest of the URL's on this page.
    i = 0


first_agency()

time.sleep(30)                                                                               # keeps tab open for 20 seconds
driver.quit()                                                                               # closes window, ends program

