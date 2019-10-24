# coding:utf8
from selenium import webdriver
import time

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)


driver.get('https://www.baidu.com/')

# title=driver.title

url=driver.current_url

# print(title)
print(url)

driver.find_element_by_id('kw').send_keys('松勤\n')

driver.find_elements_by_id('1')

url2=driver.current_url
print(url2)
# title2 = driver.title
# print(title2)

#截屏
driver.get_screenshot_as_file('baidu.png')


# title=driver.find_element_by_tag_name('title')
# print(title.text)
# print(driver.title)
#
# driver.find_element_by_id("kw").send_keys('松勤\n')
# driver.find_element_by_id('1')
# # time.sleep(1)
# print(driver.title)

input('........')
driver.quit()