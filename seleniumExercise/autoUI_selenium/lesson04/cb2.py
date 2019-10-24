# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

# 打开网址
driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson04/cb.html')

checkedEles = driver.find_elements_by_css_selector('input[name=vehicle][checked]')


for one in checkedEles:
    one.click()

driver.find_element(By.CSS_SELECTOR,"input[value=car]").click()



input('press any key to quit...')
driver.quit()   # 浏览器退出