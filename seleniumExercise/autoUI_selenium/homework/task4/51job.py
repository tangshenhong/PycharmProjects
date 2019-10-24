# coding:utf8
import time

from selenium import webdriver
executable_path = r"d:\tools\webdrivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path)
# 别忘了设置
driver.implicitly_wait(10)

# 打开网址
driver.get('http://www.51job.com')

# 选择高级搜索 ， 可以用 a[href*=advance_search]  也可以用 div.ush > a 或者 .more
driver.find_element_by_css_selector('a.more').click()


# 输入选择关键词
driver.find_element_by_id('kwdselectid').send_keys('python')

# 工作地点选择
driver.find_element_by_id('work_position_input').click()

# 取消 已经选择的
selectedCityEles = driver.find_elements_by_css_selector('#work_position_click_center em[class=on]')

for one in selectedCityEles:
    one.click()

# 选杭州
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()

# 保存选择
driver.find_element_by_id('work_position_click_bottom_save').click()


# 先不加下面这行代码，给大家看看有什么问题

# 要点一下别的地方， 否则下面的元素会被挡住， driver.find_element_by_css_selector('.tit').click()
driver.find_element_by_css_selector('.c.c_h>label').click()


# 职能类别 选 计算机软件 -> 高级软件工程师

driver.find_element_by_id('funtype_click').click()


driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()

driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()


driver.find_element_by_id('funtype_click_bottom_save').click()

# 公司性质选 外资 欧美
driver.find_element_by_id('cottype_list').click()

cottype_list=driver.find_elements_by_css_selector('#cottype_list .ul>span')


#模拟点击键盘向下按键
import win32com.client
#需要先安装pypiwin32库，安装好了之后重启下pycharm
#官方文档：http://timgolden.me.uk/pywin32-docs/win32api__keybd_event_meth.html
#键盘对应参数：https://docs.microsoft.com/zh-cn/windows/desktop/inputdev/virtual-key-codes
import win32api
import win32con

shell = win32com.client.Dispatch("WScript.Shell")
for i in range(len(cottype_list)):
    win32api.keybd_event(win32con.VK_DOWN, 0, 0, 0)
    time.sleep(0.5)
#模拟回车符号
# win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)

# 先直接写span[data-value="01"] 发现有多个
driver.find_element_by_css_selector('#cottype_list span[title*="欧美"]').click()




# 工作年限选
driver.find_element_by_id('workyear_list').click()
driver.find_element_by_css_selector('#workyear_list span[data-value="02"]').click()

# 点击搜索
# ！！！ 注意有时候运行环境和调试环境不一样，需要多一些限制#

driver.find_element_by_css_selector(
'span.p_but[onclick^=kwdGoSearch]').click()

# 结果列表获取内容
jobs = driver.find_elements_by_css_selector('#resultList div[class=el]')


for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    stringFilelds = [field.text for field in fields]
    print (' | '.join(stringFilelds))


driver.quit()
