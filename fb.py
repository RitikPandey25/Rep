from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options

browser = webdriver.Firefox(executable_path="./gecko")

browser.get("https://en-gb.facebook.com/")
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("ritikpandey25@gmail.com")
password.send_keys("p")
submit.click()
p.find_element_by_css_selector("div[aria-label='Search Facebook']").send_keys("llll")
p1.find_element_by_css_selector("button[aria-label='Search']").click()
