# coding:utf8
from selenium import webdriver


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('http://www.baidu.com')


element_keyword = driver.find_element_by_id("kw")
element_keyword.send_keys('松勤')

element_search_button = driver.find_element_by_id("su")
element_search_button.click()


# ================================
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
ele = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID,'1')))

driver.implicitly_wait(10)

#做一些耗时的操作


driver.implicitly_wait(10)



print(ele.text)

if ele.text.startswith('松勤网 - 松勤软件测试-软件测试在线教育领跑者'):
    print('pass')
else:
    print('fail')

# ================================
driver.quit()