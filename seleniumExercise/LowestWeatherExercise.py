#本练习用于获取http://www.weather.com.cn/html/province/fujian.shtml中的最低温城市
from selenium import webdriver
#处理城市元素，获取对应的城市名称、低温
def findcityweather(cityweather):
    cityname=cityweather.find_element_by_tag_name('dt').text
    low_temp=int(cityweather.find_element_by_tag_name('dd').text.split('℃/')[0])
    citynames.append(cityname)
    low_temps.append(low_temp)
#城市名称列表
citynames=[]
#城市低温列表
low_temps=[]
driver=webdriver.Chrome('F:\selenium\driver\chromedriver')
driver.get('http://www.weather.com.cn/html/province/fujian.shtml')
#获得所有城市的元素
cityweathers=driver.find_element_by_id('forecastID').find_elements_by_tag_name('dl')
for one in cityweathers:
    findcityweather(one)
#获取最低温
lowest_temp=min(low_temps)
print('最低气温为：%s℃,城市有'%lowest_temp,end='')
#打印最低温城市
for i,one in enumerate(low_temps):
    if one==lowest_temp:
        print(citynames[i],end=' ')
driver.quit()

