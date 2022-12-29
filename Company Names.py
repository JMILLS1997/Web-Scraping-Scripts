import requests
from bs4 import BeautifulSoup

#Global Variables:
url = 'https://www.agencycentral.co.uk/agencysearch/engineering/agencysearch.htm'
class_list = []
scrap = ['order', 'emp_cand', 'skill']

page = requests.get(url)                                   # use requests to access page found through URL link
soup = BeautifulSoup(page.content, "html.parser")          # parse HTML data from accessed page
tags = soup.find_all()                                     # find all tags within 'soup'

def scrap_data():                                          # useless info with same tag: 'data-name', removed
        for i in scrap:
            for j in class_list:
                if i == j:
                    class_list.remove(i)

def names():
    for tag in tags:                                       # iterate all tags
        if tag.has_attr("data-name"):                      # if tag has attribute of class
            if len(tag["data-name"]) != 0:                 # and if length of characters in the tag does not = 0
                class_list.append(tag['data-name'])        # append 'tag' info to 'class_list'
                scrap_data()                               # run function to remove useless data

names()
print(class_list)