
from selenium import webdriver
import traceback

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

def fun(driver):
    t1 = driver.find_element_by_id('1t')
    t2 = driver.find_element_by_id('t2')
    t3 = driver.find_element_by_id('t3')

try:
    driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson07/ac.html')
    fun(driver)

except:
    # print(traceback.format_exc())
    print('代码出错，检查你的代码')

finally:
    driver.quit()

