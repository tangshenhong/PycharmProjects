# coding=utf-8
from selenium import webdriver
import  time


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

# driver.get('https://www.baidu.com/')
#
#
# # --------------截图百度LOGO---------------
# driver.get_screenshot_as_file('d:/shot.png')
#
# ele = driver.find_element_by_css_selector('img[src="//www.baidu.com/img/bd_logo1.png"]')
# ele.screenshot('button.png')
# ----------------------------------

#---------截图网易云音乐------------

driver.get('https://music.163.com/')
#切到frame里面定位元素
driver.switch_to.frame('g_iframe')


banner=driver.find_element_by_id('index-banner')
banner.screenshot('d:\\banner.png')


input('press any key to quit...')
driver.quit()   # 浏览器退出