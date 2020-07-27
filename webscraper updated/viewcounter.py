#import urllib.request
#from bs4 import beautifulsoup


#url_list = {
#    url1 : "https://livecounts.io/live-view-count/7c2z4gqqs5e"
#}

#wiki = "https://en.wikipedia.org/wiki/list_of_state_and_union_territory_capitals_in_india"

#page = urllib.request.urlopen(wiki)

#soup = beautifulsoup(page)

#print(soup.prettify())
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from os import system

PATH = "C:\Program Files (x86)\chromedriver.exe"
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(PATH, options=op)
driver.get("https://counts.live/youtube-view-count/7C2z4GqqS5E")
sleep(5)
#while True:
search = driver.find_element_by_class_name("odometer-inside")
search_9thpos = search.text 
search_9thpos_list = list(search_9thpos)
driver.quit()

#print(search_9thpos_list)

a = 0

for i in range(0, len(search_9thpos_list)):
    if search_9thpos_list[a] == '\n':
        search_9thpos_list.pop(a)
    else:
        a += 1

search_9thpos = ''.join(search_9thpos_list)
system("cls")
print(search_9thpos)