from selenium import webdriver
import time

#如果环境变量path中有路径，可以不用写全
driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
# 别忘了设置
driver.implicitly_wait(10)

# 抓取信息
driver.get('http://www.51job.com')
driver.find_element_by_id('kwdselectid').send_keys('python')
# 点击工作地点
driver.find_element_by_id('work_position_input').click()

#为了让城市动态加载出来等待2秒
time.sleep(2)

citys=driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em')

for city in citys:
    city_name=city.text#城市名
    selected = city.get_attribute('class')#查看是否被选中
    # print(city_name)
    if city_name == '杭州':
        if selected != 'on':
            city.click()
    else:
        if selected == 'on':
            city.click()

#保存城市选择
driver.find_element_by_id('work_position_click_bottom_save').click()

#点击搜索
driver.find_element_by_css_selector('.ush.top_wrap button').click()

#搜索结果分析
jobs=driver.find_elements_by_css_selector('#resultList .el')

for job in jobs[1:]:
    #过滤掉第一行标题
    # if 'title' in job.get_attribute('class'):
    #     continue
    msgs=job.find_elements_by_tag_name('span')
    str_msgs=[msg.text for msg in msgs]
    print('|'.join(str_msgs))

driver.quit()