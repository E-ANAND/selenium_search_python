

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 

search_string = ("Write your search here")

search_string = search_string.replace(" ",'+')

browser = webdriver.Chrome('chromedriver')

for i in range(1):
    matched_elements = browser.get("https:\\www.google.com/search?q=" + search_string + "&start=" + str(i))


