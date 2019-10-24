from selenium import webdriver
import time

#如果环境变量path中有路径，可以不用写全
driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
# 别忘了设置
driver.implicitly_wait(10)

driver.get('http://www.51job.com')

#输入关键字
driver.find_element_by_css_selector('#kwdselectid').send_keys('python')

#选择城市
driver.find_element_by_css_selector('#work_position_input').click()
#留出时间加载弹出框
time.sleep(3)

selected_citys=driver.find_elements_by_css_selector('#work_position_click_multiple_selected span.ttag')

if selected_citys==[]:
    pass
else:
    for city in selected_citys:
        city.click()
#选择杭州
driver.find_element_by_css_selector('#work_position_click_center_right_list_category_000000_080200').click()

driver.find_element_by_css_selector('#work_position_click_bottom_save').click()

driver.find_element_by_css_selector('.ush button').click()

#搜索并获取结果
jobs=driver.find_elements_by_css_selector('#resultList div.el')[1:]

for job in jobs:
    job_name=job.find_element_by_css_selector('p').text
    job_comp=job.find_element_by_css_selector('span.t2').text
    job_local=job.find_element_by_css_selector('span.t3').text
    job_salary=job.find_element_by_css_selector('span.t4').text
    job_date=job.find_element_by_css_selector('span.t5').text

    print('|'.join([job_name,job_comp,job_local,job_salary,job_date]))

driver.quit()