from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import os
import time


#options=Options()
#options.headless=True
browser = webdriver.Firefox(executable_path="./gecko")
browser.get("https://time.is/GMT")

x=1

while x==1:
  time1 = browser.find_element_by_id("clock")
  str=time1.text
  print(str)
  os.system('clear')
  time.sleep(1)