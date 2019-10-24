from selenium import webdriver
driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

# ------------------------
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

ele = driver.find_element_by_id("forecastID")
print(ele.text)

''' 
citysWeather是每个城市的温度信息 list

每个元素像这样：
南京
12℃/27
'''
citysWeather = ele.text.split('℃\n')


# 算出温度最低城市

lowest = 40
lowestCity = []  # 温度最低城市列表
for one in citysWeather:
    one = one.replace('℃','')
    print(one)
    parts = one.split('\n')
    curcity=parts[0]
    lowweather = min([int(one) for one in parts[1].split('/')])
    # 发现气温更低的城市
    if lowweather<lowest:
        lowest = lowweather
        lowestCity = [curcity]
    #  温度和当前最低相同，加入列表
    elif lowweather ==lowest:
        lowestCity.append(curcity)



print('温度最低为%s℃, 城市有%s' % (lowest, ' '.join(lowestCity)))

# ------------------------

driver.quit()