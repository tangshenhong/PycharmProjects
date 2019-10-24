# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson02/s1.html') # 打开网址



from selenium.common.exceptions import NoSuchElementException

ele = driver.find_element_by_id("food")

print(ele.get_attribute('outerHTML'))

foodText=ele.get_attribute('innerHTML')
print(foodText)
ret1=foodText.split('</span>')[1]
ret2=ret1.split('class="')[1]
print(ret2.split('"')[0])

driver.quit()

