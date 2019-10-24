#-*- coding:utf-8 -*-
# @Time  :2019/6/14 12:53
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome('F:\selenium\driver\chromedriver.exe')
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
driver.implicitly_wait(10)
#出发城市 填写 ‘南京南’
fromStation=driver.find_element_by_xpath('//input[@id="fromStationText"]')
fromStation.click()
fromStation.send_keys('南京南\n')
#到达城市 填写 ‘杭州东’
toStation=driver.find_element_by_xpath("//input[@id='toStationText']")
toStation.click()
toStation.send_keys('杭州东\n')
#发车时间 选 06:00--12:00
departure_time=driver.find_element_by_xpath('//select[@id="cc_start_time"]')
Select(departure_time).select_by_visible_text('06:00--12:00')
#发车日期选当前时间的下一天，也就是日期标签栏的，第二个标签
driver.find_element_by_xpath("//input[@id='train_date']").click()
driver.find_element_by_xpath("//div[contains(@style,'background: rgb(193, 217, 255)')]/following-sibling::div[1]").click()
#点击查询
driver.find_element_by_xpath("//a[@id='query_ticket']").click()
#
queryresults=driver.find_elements_by_xpath("//tr[contains(@id,'ticket_')]")
for one in queryresults:
    second_class=one.find_element_by_xpath('./td[4]').text
    if second_class!='--':
        train_number=one.find_element_by_xpath("./td[1]//div[contains(@id,'ticket_')]").text
        print(train_number)
time.sleep(3)
driver.quit()