#-*- coding:utf-8 -*-
# @Time  :2019/6/13 10:40
from selenium import webdriver
import time

driver=webdriver.Chrome('F:\selenium\driver\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('http://www.51job.com')
#1、点击高级搜索
driver.find_element_by_css_selector('.more').click()
time.sleep(1)

#2、输入搜索关键词 python
driver.find_element_by_css_selector('#kwdselectid').send_keys('python')

#3、地区选择杭州
driver.find_element_by_css_selector('p#work_position_click').click()
time.sleep(1)
#----点选掉默认地区
selecteds=driver.find_elements_by_css_selector("[id*='work_position_click_multiple_selected_each_']")
for one in selecteds:
    one.click()
#----选择杭州
driver.find_element_by_css_selector('#work_position_click_center_right_list_category_000000_080200').click()
#----点击确认
driver.find_element_by_css_selector('#work_position_click_bottom_save').click()
time.sleep(1)

#4、职能类别 选 计算机软件 -> 高级软件工程师
jobtype=driver.find_element_by_css_selector('#funtype_click')
driver.execute_script("arguments[0].click();", jobtype)
time.sleep(1)
#----选择计算机软件
driver.find_element_by_css_selector('#funtype_click_center_right tr:nth-child(1)>td:nth-child(1)>#funtype_click_center_right_list_category_0100_0100').click()
#----选择高级软件工程师
driver.find_element_by_css_selector('.in.d0 div>span:nth-child(2)').click()
#----点击确定
driver.find_element_by_css_selector('#funtype_click_bottom_save').click()

#5、公司性质选 外资 欧美
driver.find_element_by_css_selector('#cottype_list').click()
driver.find_element_by_css_selector("#cottype_list [title='外资（欧美）']").click()

#6、工作年限选 1-3 年
workyear=driver.find_element_by_css_selector('#workyear_list').click()
workyear=driver.find_element_by_css_selector("#workyear_list [title='1-3年']").click()
#点击搜索
driver.find_element_by_css_selector('.btnbox.p_sou>.p_but').click()
time.sleep(1)

#7、搜索最新发布的职位， 抓取页面信息
resultlist=driver.find_elements_by_css_selector('#resultList>div:nth-child(4)>*')
ouputresult=[]
for one in resultlist:
    ouputresult.append(one.text)
print('|'.join(ouputresult))

driver.quit()