
from selenium import webdriver

import time

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)


driver.get('https://tinypng.com/')
print(driver.title)

driver.find_element_by_css_selector("figure.icon").click()



time.sleep(3)

# 直接发送键盘消息给 当前应用程序，
# 前提是浏览器必须是当前应用
#   pip install pypiwin32
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")


# 有的系统要加 '\r'
# 有的系统要加 '\r\n'
shell.Sendkeys(r"d:\banner.png" + '\n')




input('...')

driver.quit()