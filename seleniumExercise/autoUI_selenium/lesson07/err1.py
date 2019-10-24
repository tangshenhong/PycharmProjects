# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson07/ac.html')


try:

    t1 = driver.find_element_by_id('1t')
    t2 = driver.find_element_by_id('t2')
    t3 = driver.find_element_by_id('n3')

except:
    print('出错了')

finally:
    driver.quit()






