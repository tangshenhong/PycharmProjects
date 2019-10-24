# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson05/xpath.html')


# eles = driver.find_elements_by_css_selector("#food>p:nth-of-type(2)")
# eles = driver.find_elements_by_css_selector("#food>p:nth-child(4)")
# eles = driver.find_elements_by_tag_name('span')
# eles=driver.find_element_by_xpath('//span[@id="beef"]/..')

ele=driver.find_element_by_xpath('//*[@id="beef"]/..')
print(ele.text.split()[0])

# print(eles.text.split()[0])

# for ele in eles:
#     print('----------')
#     print(ele.get_attribute('outerHTML'))

# raw_input('press any key to quit...')
driver.quit()

