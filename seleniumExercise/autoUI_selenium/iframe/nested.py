# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/iframe/nested.html')

driver.switch_to.frame('layer2')
driver.switch_to.frame('layer3')

input1 = driver.find_element_by_tag_name("input")
input1.send_keys('输入layer2')

driver.switch_to.parent_frame()
input1 = driver.find_element_by_tag_name("input")
input1.send_keys('输入layer1')

driver.switch_to.default_content()
input1 = driver.find_element_by_tag_name("input")
input1.send_keys('输入最外层')

input('press any key to quit...')
driver.quit()