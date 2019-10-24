from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.vmall.com/")  # 模拟鼠标操作-鼠标悬浮菜单-淘宝网首页地区选择
sleep(1)

# 获取要悬浮的元素，并使用move_to_element()方法
element_list = driver.find_element_by_xpath("//*[@id='zxnav_1']")
ac=ActionChains(driver)
ac=ac.move_to_element(element_list).perform()


sleep(1)
# 悬浮元素出现菜单后，可以点击悬浮菜单里的元素了,这里选择“全球”
# driver.find_element_by_css_selector('#J_SiteNavRegionList > li:nth-child(1)').click()

driver.quit()