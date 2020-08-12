from selenium import webdriver
from time import sleep

browser = webdriver.Chrome('./chromedriver(1).exe')
browser.maximize_window()
browser.get('http://www.baidu.com/')
browser.find_element_by_id('kw').send_keys('百变小樱')
sleep(0.5)
browser.find_element_by_id('su').click()
sleep(3)
# browser.quit()
