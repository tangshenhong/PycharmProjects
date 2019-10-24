# coding=utf8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson02/s1.html') # 打开网址




# ele = driver.find_element_by_id("food")
# print(ele.text)








try:
    ele = driver.find_element_by_id("foodee")
except NoSuchElementException:
    print('NoSuchElementException')

# from selenium.webdriver.common.by import By
# ele = driver.find_element(by=By.ID, value="222")



driver.quit()

