# coding=utf-8
from selenium import webdriver
import  time


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('http://ci.ytesting.com/student/login/login.html')

# ----------------------------------
driver.find_element_by_id('username').send_keys('abcdefg')#随便填一个用户名
driver.find_element_by_id('password').send_keys('abcdefg')#随便填一个密码

driver.find_element_by_id('submit').click()

time.sleep(3)#等弹出框
driver.find_element_by_css_selector('.bootstrap-dialog-footer-buttons button').click()


# ----------------------------------
input('press any key to quit...')
driver.quit()   # 浏览器退出