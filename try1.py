

from selenium import webdriver
import time
url = "http://www.baidu.com"
dr = webdriver.Firefox()
dr.get(url)
dr.maximize_window()
dr.find_element_by_id('kw').send_keys("python")
dr.find_element_by_id('su').click()
time.sleep(5)
dr.quit()