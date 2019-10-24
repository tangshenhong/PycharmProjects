from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

from_st=driver.find_element_by_id('fromStationText')
from_st.click()
from_st.send_keys('南京南\n')

toStation=driver.find_element_by_id('toStationText')
toStation.click()
toStation.send_keys('杭州东\n')


select=Select(driver.find_element_by_id('cc_start_time'))
select.select_by_visible_text('06:00--12:00')

#选择日期
driver.find_element_by_xpath('//*[@id="date_range"]/ul/li[2]').click()

#//*[@id="queryLeftTable"]/tr/td[4][@class]/preceding-sibling::td[last()]//a

#//*[@id="queryLeftTable"]/tr/td[4][@class]/../td[1]//a

trains=driver.find_elements_by_xpath('//*[@id="queryLeftTable"]/tr/td[4][@class]/../td[1]//a')

for train in trains:
    print(train.text)


driver.quit()

