from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('chromedriver')
driver.get('https://sports.daum.net/team/EPL/249#1')

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
thumnails = soup.select('#viewNews > div > ul:nth-child(2) > li > a > img')

for thumnail in thumnails:
    print(thumnail['src'])

driver.quit()
