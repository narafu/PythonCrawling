import dload
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.starbucks.co.kr/menu/drink_list.do")

soup = BeautifulSoup(driver.page_source, 'html.parser')

menuDrinks = soup.select('#container .product_list li a > img')

# i = 1
for menuDrink in menuDrinks:
    # print(f'{i}', menuDrink['alt'], menuDrink['src'])
    # i += 1
    dload.save(menuDrink['src'], f"imgs/product/{menuDrink['alt']}.jpg")

driver.quit()
