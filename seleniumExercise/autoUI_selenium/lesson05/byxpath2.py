# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson05/s1.html')

many = driver.find_element_by_id("many")

eles=many.find_elements_by_xpath('.//span')

# eles = food.find_elements_by_xpath('./p')
# eles=food.find_elements_by_xpath('./p[@id="xx"]')


for ele in eles:
    print('----------')
    print(ele.get_attribute('outerHTML'))

# raw_input('press any key to quit...')
driver.quit()

