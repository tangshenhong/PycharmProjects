# coding:utf8
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

executable_path = r"d:\tools\webdrivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path)
# 别忘了设置
driver.implicitly_wait(10)

# 打开网址
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

#出发地
from_st=driver.find_element_by_id('fromStationText')
from_st.click()
from_st.send_keys('南京南\n')

#目的地
to_st=driver.find_element_by_id('toStationText')
to_st.click()
to_st.send_keys('杭州东\n')
#发车时间
start_time=Select(driver.find_element_by_id('cc_start_time'))
start_time.select_by_visible_text('06:00--12:00')

#选择第二天作为发车日期
driver.find_element_by_css_selector('#date_range>ul>li:nth-child(2)').click()

#取出所有二等座有票的车次信息
train_eles=driver.find_elements_by_xpath('//tbody[@id="queryLeftTable"][1]//td[4][@class]/../td[1]//a')

#打印所有
for t in train_eles:
    print(t.text)

driver.quit()