# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson04/s1.html')


eles = driver.find_elements_by_css_selector(
    "#food>*")

for ele in eles:
    print(ele.get_attribute('outerHTML'))

# raw_input('press any key to quit...')
driver.quit()

