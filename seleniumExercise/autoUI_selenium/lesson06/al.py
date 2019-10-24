# coding=utf-8
from selenium import webdriver
import  time


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson06/al.html')


# ----------------------------------
driver.find_element_by_id('b3').click()

time.sleep(2)
# driver.switch_to.alert.accept()

driver.switch_to.alert.send_keys('你好selenium')
msg=driver.switch_to.alert.text
driver.switch_to.alert.accept()



print(msg)
time.sleep(2)
# txt=driver.switch_to.alert.text
# print(txt)

# driver.switch_to.alert.send_keys('你好')
# driver.find_element_by_id('other').click()














# -------------------------------------
input('press any key to quit...')
driver.quit()   # 浏览器退出