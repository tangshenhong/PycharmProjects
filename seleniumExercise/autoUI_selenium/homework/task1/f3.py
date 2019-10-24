from selenium import webdriver
driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

ele = driver.find_element_by_id("forecastID")

# -----------------------------------
# 再用bs4分析
html_doc = ele.get_attribute('innerHTML')

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "html5lib")

# 发现每个城市的信息都在dl里面
dls = soup.find_all('dl')

# 将城市和气温信息保存到列表citys中
citys = []
for dl in dls:
    name = dl.dt.a.string
    ltemp1 = dl.dd.b.string.replace('℃','')
    ltemp2 = dl.dd.span.string.replace('℃','')
    ltemp = min(int(ltemp1),int(ltemp2))
    print(name, ltemp)
    citys.append([name,ltemp])


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

driver.quit()