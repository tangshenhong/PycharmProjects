# coding=utf-8
import time

from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('https://www.baidu.com/')
# title=driver.find_element_by_tag_name('title')
# print(title.text)
# print(driver.title)

driver.find_element_by_id("kw").send_keys('松勤\n')
time.sleep(1)

driver.find_element_by_css_selector('div[id="1"] h3.t>a').click()
time.sleep(2)
# print(driver.title)





time.sleep(5)


handles=driver.window_handles
baidu_handle=driver.current_window_handle

for handle in handles:
    driver.switch_to.window(handle)
    if '松勤网 - 松勤软件测试' in driver.title:
        print('切进来了')
        break
print(driver.current_window_handle)

#点击全部课程分类
driver.find_element_by_css_selector('span.navbar-brand>a[href="/course/explore"]').click()

driver.switch_to.window(baidu_handle)
driver.find_element_by_id("kw").send_keys('成功切换')
driver.close()

driver.quit()


