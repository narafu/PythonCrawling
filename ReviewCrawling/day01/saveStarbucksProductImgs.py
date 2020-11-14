from selenium import webdriver
from bs4 import BeautifulSoup as bs
import dload
import os


def createDirectory(root):
    try:
        if not os.path.exists(root):
            os.makedirs(root)
    except OSError:
        print(f'{root} error')


def getImgs(idx):
    pass


browser = webdriver.Chrome('chromedriver.exe')

# 구글 검색페이지
browser.get('https://www.google.co.kr/')

# '스타벅스' 검색
browser.find_element_by_css_selector(
    '#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input').send_keys('스타벅스')
browser.find_element_by_css_selector(
    '#tsf > div:nth-child(2) > div.A8SBwf > div.FPdoLc.tfB0Bf > center > input.gNO89b').click()

# 스타벅스 상품페이지
browser.find_element_by_css_selector(
    '#rso > div:nth-child(1) > div > table > tbody > tr.mslg.c9EJob > td:nth-child(1) > div > span > h3 > a').click()

# productHtml
productHtml = browser.page_source
soup = bs(productHtml, 'html.parser')

# 타이틀 크롤링
titles = soup.select('#product_view_tab01 > div.product_list > dl > dt > a')

for idx, title in enumerate(titles):
    # 폴더생성
    createDirectory(f'imgs/{title.text}')
    # 이미지 크롤링
    getImgs(idx)
    imgs = soup.select(
        f'#product_view_tab01 > div.product_list > dl > dd:nth-child({(idx + 1) * 2}) > ul > li > dl > dt > a > img')
    # 이미지 저장
    for i, img in enumerate(imgs):
        dload.save(img['src'], f'imgs/{title.text}/{title.text}{1 + i}.jpg')
    print(f'<<< {title.text} 완료 >>>')

browser.quit()
