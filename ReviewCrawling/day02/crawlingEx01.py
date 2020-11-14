from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('../chromedriver.exe')
soup = BeautifulSoup(driver.page_source, 'html.parser')

# driver.quit()
