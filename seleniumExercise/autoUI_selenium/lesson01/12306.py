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

#发车日期
start_date=driver.find_element_by_css_selector('#date_range ul>li:nth-child(2)')
start_date.click()

time.sleep(3)
#找二等座
css="#queryLeftTable tr[id^='ticket']>td.yes:nth-child(4),#queryLeftTable tr[id^='ticket']>td.t-num:nth-child(4)"

xpath_yes="//*[@id='queryLeftTable']/tr[contains(@id,'ticket')]/td[4][@class='yes']/preceding-sibling::td[last()]// a"

xpath_tnum="//*[@id='queryLeftTable']/tr[contains(@id,'ticket')]/td[4][@class='t-num']/preceding-sibling::td[last()]// a"

trains=driver.find_elements_by_xpath(xpath_yes+'|'+xpath_tnum)
print('符合条件的车次有:')
for t in trains:
    print(t.text)

driver.execute_script('')

driver.quit()