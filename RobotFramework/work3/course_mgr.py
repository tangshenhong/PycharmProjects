from selenium import webdriver
import time
driver=webdriver.Chrome()
def login():
    driver.implicitly_wait(10)
    driver.get('http://localhost:8080/mgr/login/login.html')
    driver.find_element_by_css_selector('#username').send_keys('auto')
    driver.find_element_by_css_selector('#password').send_keys('sdfsdfsdf')
    driver.find_element_by_css_selector('.btn.btn-success').click()
    time.sleep(1)
def deleteAllCourse():
    login()

