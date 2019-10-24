# coding:utf8
import time

from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)



driver.get('http://music.163.com')
# driver.set_window_size(800,600)

driver.execute_script('window.scrollBy(200,0)')

searchbox = driver.find_element_by_css_selector('#g_search input')

time.sleep(1)
# driver.find_element_by_css_selector('#g_search label').click()
searchbox.send_keys('张学友\n')



driver.quit()