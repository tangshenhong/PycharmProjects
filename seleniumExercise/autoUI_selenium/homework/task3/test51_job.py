from selenium import webdriver
import time

#如果环境变量path中有路径，可以不用写全
driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
# 别忘了设置
driver.implicitly_wait(10)

# 抓取信息
driver.get('http://www.51job.com')

#输入职位名称
driver.find_element_by_id('kwdselectid').send_keys('Python')

#点击工作地点
driver.find_element_by_id('work_position_input').click()

time.sleep(1)

#获取所有城市
cityeles=driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em')

for one in cityeles:
    cityName=one.text
    selected=one.get_attribute('class')
    if selected =='on':
        if cityName !='杭州':
            one.click()
    else:
        if cityName =='杭州':
            one.click()
#保存选择
driver.find_element_by_id('work_position_click_bottom_save').click()

#点击搜索
driver.find_element_by_css_selector('.ush button').click()

#搜索结果分析
jobs=driver.find_elements_by_css_selector('#resultList div[class=el]')

for job in jobs:
    # if 'title' in job.get_attribute('class'):
    #     continue
    fields=job.find_elements_by_tag_name('span')
    strField= [field.text for field in fields]
    print('|'.join(strField))

driver.quit()

















