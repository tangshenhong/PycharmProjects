import time

from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
# driver = webdriver.Firefox(r'd:\tools\webdrivers')

driver.get('https://music.163.com/') # 打开网址

time.sleep(3)
# -----------------------------------
title=driver.find_element_by_tag_name('iframe').get_attribute('name')
print(title)

# -----------------------------------


# input('press any key to quit...')
driver.quit()

