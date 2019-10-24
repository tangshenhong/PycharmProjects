# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson02/s1.html') # 打开网址


ele = driver.find_element_by_id("choose_car")
carsHtml = ele.get_attribute('innerHTML')
print(carsHtml)

driver.quit()