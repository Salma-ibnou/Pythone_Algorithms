from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# create  the browser instance 
browser = webdriver.Chrome('chromedriver.exe')
sleep(1)

browser.maximize_window()
sleep(1)

browser.get('http://172.17.43.12/')