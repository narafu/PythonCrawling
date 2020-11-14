from bs4 import BeautifulSoup
from openpyxl import Workbook
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.starbucks.co.kr/menu/drink_list.do")

soup = BeautifulSoup(driver.page_source, 'html.parser')

wb = Workbook()
ws1 = wb.active
ws1.title = "StarburksMenu"
ws1.append(["제품명", "이미지"])

menuDrinks = soup.select('#container .product_list li a > img')

for menuDrink in menuDrinks:
    title = menuDrink['alt']
    img = menuDrink['src']
    ws1.append([title, img])

driver.quit()
wb.save(filename="StarburksMenu.xlsx")
