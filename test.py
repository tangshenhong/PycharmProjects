from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.execute_script('window.open("http://127.0.0.1:8081/Systems/Home/Index1")')
driver.close()
