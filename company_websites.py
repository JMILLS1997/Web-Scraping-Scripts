##################################################################################################
#: opens up website for agency central and crawls through to the recruitment agency website.
# future improvements:
#   - click on next page once all data for current agencies on page is collected - IMPLEMENTED
#   - upload data into excel alongside the "company_name" script - SEE OTHER SCRIPTS
##################################################################################################



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as EX
import pickle
import time



def load_cookies():  
        cookies1 = pickle.load(open('cookies1.pkl', 'rb'))                                              # loads cookies to the browser
        for cookie1 in cookies1:
            driver.add_cookie(cookie1)
        driver.refresh()                                                                                # refresh page to implement cookies loaded previously



def location():
    time.sleep(5)                                                                                       # needs a manual wait for driver to update with current tab('window') count
    if len(driver.window_handles) == 1:
        try:
            WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="agency-branch-selection"]/div[3]/div/ul/li/span[1]'))).click()        
        finally:
            pass
    else:
        pass 



def window():
    time.sleep(3)
    if len(driver.window_handles) == 2:
        driver.close()
    elif len(driver.window_handles) == 1:
        pass



def url_collect():
    try:
        time.sleep(3)
        url_collect = driver.current_url                                                             # collects current tab's URL                                                             
        agency_url_list.append(url_collect)
        print(url_collect)
        window()                                                                                     # appends collected URL data to list "url_list"
    finally:
        pass



def next_page_url():
    global x
    try:
        time.sleep(3)
        next_page_url_collect = driver.current_url                                                   # collects current tab's URL                                                             
        ac_url_list.append(next_page_url_collect)
        window()                                                                                     # appends collected URL data to list "url_list"
    except:
        pass
    x = x + 1



def next_page():
    time.sleep(2)
    try:
        next_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search-results-container"]/ul/li[13]/a')))
        next = next_button.get_attribute('href')
        driver.get(next)
        
    except EX:
        driver.quit()



def agency_url():                                                                                                                                       # to iterate through the data collected by "elements".                                                                                     
        elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="contact-button-visit-website"]')))
        for element in elements:                                                                                                                       # for each instance of data collected in the list "elements"...        
            element.click()                                                                                                                        # click on the relvant element  
            location()                                                                                                                                  # runs "location"                           
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))                                                                              # driver waits for number of tabs to = 2 before moving onto next operation
            new_tab = driver.window_handles[1]                                                                                                          # window handles is a list of the various tabs open in a browser
            driver.switch_to.window(new_tab)                                                                                                            # switches focus to new tab
            url_collect()                                                                                                                               # closes current tab
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(1))                                                                              # waits for driver to see total number of tabs = 1
            driver.switch_to.window(driver.window_handles[0])                                                                                           # focuses on orignal tab
            time.sleep(3)



def website_open():
    global driver
    options = webdriver.ChromeOptions()                                                                     # allows for use of ChromeDriver without exceptions flagging up or other bugs that are yet to be removed.
   #options.headless = True                                                                                 # from what I can tell, headless options does not work for all websites so plan is to keep this headed.
    options.add_experimental_option('excludeSwitches', ['enable-logging'])                       
    driver = webdriver.Chrome(options=options)
    driver.get(ac_url_list[x])



def initiate_data_collection():
    x = 0
    agency_url_list = []                                                                                           # blank list to contain all collected URL's. Will be added to excel at a later stage.
    ac_url_list = ["https://www.agencycentral.co.uk/agencysearch/engineering/agencysearch.htm"]

    for a in ac_url_list:
        website_open()
        load_cookies()
        agency_url()
        next_page()
        next_page_url()
        driver.quit()