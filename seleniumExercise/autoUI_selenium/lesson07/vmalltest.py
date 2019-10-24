from selenium import  webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)


driver.get('https://www.vmall.com/')
main_handel=driver.current_window_handle

#进入华为官网
driver.find_element_by_css_selector('[href="http://consumer.huawei.com/cn/"]').click()

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if '华为消费者业务官网' in driver.title:
        break


eles=driver.find_elements_by_css_selector('.nav-wrap ul.nav-cnt>li')
menus= [ele.text for ele in eles]
print(menus)
expect='''智能手机
  笔记本
  平板
  穿戴设备
  智能家居
  更多产品
  软件应用
  服务与支持'''
expect= [exp.strip() for exp in expect.splitlines()]

if menus == expect:
    print('pass')
else:
    print('fail')

#切回去
driver.switch_to.window(main_handel)

element_list = driver.find_element_by_xpath("//*[@id='zxnav_1']")
ac=ActionChains(driver)
ac=ac.move_to_element(element_list).perform()

eles=driver.find_elements_by_css_selector('#zxnav_1 .category-panels li.subcate-item span')

menus=[ele.text for ele in eles]

if "平板电脑 笔记本电脑 笔记本配件" == ' '.join(menus):
    print('success')
else:
    print('fail')

driver.quit()





