import time

from selenium import webdriver
# from selenium.webdriver.chrome import options
# chromeoption=options.Options()
# chromeoption.add_argument('disable-infobars')
# chromeoption.add_argument('--start-maximized')

driver=webdriver.Chrome()
# from selenium.webdriver.common.by import By

# driver=webdriver.Firefox()

#访问百度
driver.get('https://baidu.com/')

# input1=driver.find_element(by=By.ID,value='kw')
input1=driver.find_element_by_id('kw')

input1.send_keys('松勤')

btn=driver.find_element_by_id('su')
btn.click()

time.sleep(1)
#获取百度松勤结果第一条
res=driver.find_element_by_id('1')

print(res.text)
if '松勤网 - 松勤软件测试' in res.text:
    print('pass')
else:
    print('fail')



driver.quit()
