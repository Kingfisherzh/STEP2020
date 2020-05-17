# -*- coding: UTF-8 -*-
import sys
import urllib
import time
from selenium import webdriver
from bs4 import BeautifulSoup


url = 'https://icanhazwordz.appspot.com/'
driver = webdriver.Chrome()
driver.get(url)

a = 'O'

driver.find_element_by_xpath("//div[contains(text(),'" + a + "')]").click()

time.sleep(2)
driver.quit()





