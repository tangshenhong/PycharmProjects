# coding:utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)



driver.get('http://music.163.com')


# 结果像这样 {'width': 855, 'height': 922}
size = driver.get_window_size()
# 只改变宽度
driver.set_window_size(1300, size['height'])
driver.set_window_size(size['width'], 600)
driver.set_window_size(800,600)

driver.maximize_window()


searchbox = driver.find_element_by_css_selector('#srch')


searchbox.send_keys('张学友\n')




driver.quit()