# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson03/s1.html')


# ele = driver.find_element_by_css_selector('button')
# print(ele.get_attribute('outerHTML'))

eles = driver.find_elements_by_css_selector('.vegetable.good')
# eles = driver.find_elements_by_tag_name('option')
for ele in eles:
    print(ele.text)
# print(eles.text)
# for ele in eles:
#     print(ele.get_attribute('outerHTML'))

# raw_input('press any key to quit...')
driver.quit()

