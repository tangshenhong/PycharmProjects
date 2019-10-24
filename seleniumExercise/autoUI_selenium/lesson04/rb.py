# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

executable_path = r"d:\tools\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path)

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson04/rb.html')


# 这里使用了根据属性值来查找
input1 = driver.find_element_by_css_selector("input[value=other]")
input1.click()


input('press any key to quit...')
driver.quit()   # 浏览器退出