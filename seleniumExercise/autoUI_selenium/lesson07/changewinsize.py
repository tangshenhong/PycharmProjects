# coding:utf8
import time

from selenium import webdriver
executable_path = r"d:\tools\webdrivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path)
driver.implicitly_wait(10)


driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson07/winsize.html')

searchbox = driver.find_element_by_tag_name('input')

#
# for i in range(10):
#     driver.execute_script('window.scrollBy(0,220)')
#
#     time.sleep(0.5)
size=driver.get_window_size()
driver.set_window_size(size['width'],600)
# driver.maximize_window()

print(size)
searchbox.send_keys('你好啊\n')


# input('...')
driver.quit()