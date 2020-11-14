from selenium import webdriver

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://nid.naver.com/nidlogin.login')

naver_id = 'wheatal1'
naver_pw = 'dosqjxj0725#'

browser.find_element_by_id('id').send_keys(naver_id)
browser.find_element_by_id('pw').send_keys(naver_pw)
browser.find_element_by_css_selector('#log\.login').click()

browser.quit()