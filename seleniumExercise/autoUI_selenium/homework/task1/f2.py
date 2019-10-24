from selenium import webdriver
driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")


driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

ele = driver.find_element_by_id("forecastID")
print(ele.text)


# 再从 forecastID 元素获取所有子元素dl
dls = ele.find_elements_by_tag_name('dl')

# 将城市和气温信息保存到列表citys中
citys = []
for dl in dls:
    # print dl.get_attribute('innerHTML')

    name = dl.find_element_by_tag_name('dt').text
    # 最高最低气温位置会变，根据位置决定是span还是b
    ltemp = dl.find_element_by_tag_name('span').text

    ltemp = int(ltemp.replace('℃',''))
    print(name, ltemp)
    citys.append((name, ltemp))

lowest = None
lowestCitys = []  # 温度最低城市列表
for one in citys:
    curcity = one[0]
    ltemp = one[1]
    # 发现气温更低的城市
    if lowest==None or ltemp<lowest:
        lowest = ltemp
        lowestCitys = [curcity]
    #  温度和当前最低相同，加入列表
    elif ltemp ==lowest:
        lowestCitys.append(curcity)

print('温度最低为%s℃, 城市有%s' % (lowest, ' '.join(lowestCitys)))