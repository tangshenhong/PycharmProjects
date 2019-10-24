# -*- coding: utf-8 -*-
from selenium import webdriver


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson04/input1.html') # 打开网址


input1 = driver.find_element_by_id("ta1")

input1.send_keys('青玉')

# print(input1.text)
# input1.clear()
print(input1.get_attribute('value'))

# ta1 = driver.find_element_by_id("ta1")
# ta1.send_keys(u'春眠不觉晓\n处处闻啼鸟')



input('press any key to quit...')
driver.quit()