from selenium import webdriver
import time

#如果环境变量path中有路径，可以不用写全
driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
# 别忘了设置
driver.implicitly_wait(10)

# 抓取信息
driver.get('http://www.51job.com')

#输入关键字
driver.find_element_by_id('kwdselectid').send_keys('python')
#点击工作地点
driver.find_element_by_id('work_position_input').click()

time.sleep(2)
citys=driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em')

#筛选城市
for city in citys:
    city_name=city.text
    isselected=city.get_attribute('class')
    if city_name == '杭州':
        if isselected != 'on':
            city.click()
    else:
        if isselected == 'on':
            city.click()

#保存选择
driver.find_element_by_id('work_position_click_bottom_save').click()

#点击搜索
driver.find_element_by_css_selector('div.ush.top_wrap button').click()

#抓取搜索结果
jobs=driver.find_elements_by_css_selector('#resultList div.el')

for job in jobs[1:]:
    job_msgs=job.find_elements_by_tag_name('span')
    msgs=[msg.text for msg in job_msgs]
    print('|'.join(msgs))


driver.quit()