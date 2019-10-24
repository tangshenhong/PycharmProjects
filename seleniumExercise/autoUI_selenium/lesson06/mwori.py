# coding=utf-8
import time

from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('https://www.baidu.com/')
# title=driver.find_element_by_tag_name('title')
# print(title.text)
print(driver.title)

driver.find_element_by_id("kw").send_keys('松勤\n')
time.sleep(1)
driver.find_element_by_css_selector('div[id="1"] h3.t>a').click()
time.sleep(1)
print(driver.title)

main_handle=driver.current_window_handle
print(main_handle)

handles=driver.window_handles
print(handles)

for handle in handles:
    # print(handle)
    driver.switch_to.window(handle)
    if '松勤网 - 松勤软件测试' in driver.title:
        print('成功跳转')
        print(driver.current_window_handle)
        break


#点击全部课程分类
driver.find_element_by_css_selector('a[href="/course/explore"]').click()

time.sleep(3)
driver.close()
driver.switch_to.window(main_handle)
print(driver.title)

input('........')
driver.quit()

