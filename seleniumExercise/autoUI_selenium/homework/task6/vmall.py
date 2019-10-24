import random

from selenium import  webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)


driver.get('https://www.vmall.com/')

#点击华为官网
driver.find_element_by_css_selector(
    'a[href="http://consumer.huawei.com/cn/"]'
).click()


# driver.find_element_by_css_selector(
#     '.s-sub li:nth-last-child(1)'
# ).click()

# driver.find_element_by_css_selector(
#     'a[href="http://appstore.huawei.com/"]'
# ).click()


def checkHuaWei():
    expected = '智能手机|笔记本|平板|智能穿戴|智能家居|更多产品|软件应用|服务与支持'

    # 注意窗口的宽度决定显示多少个菜单，可能需要拉宽窗口
    # 先不写下面的代码，发现错误再添加
    # size = driver.get_window_size()
    # driver.set_window_size(1520, size['height'])
    #
    # eles = driver.find_elements_by_css_selector(".left-box .nav-cnt > li")
    eles=driver.find_elements_by_css_selector('ul.nav-cnt a[lab="<page title>"]')
    eleTexts = [ele.text for ele in eles]


    actual = '|'.join(eleTexts)
    if actual == expected:
        print('huawei page pass')
    else:
        print('huawei page fail!!!!')
        print(actual)
        print(expected)


def checkAppmarket():
    expected = '''首页|游戏|软件|专题|品牌专区|华为软件专区'''

    eles = driver.find_elements_by_css_selector("ul.ul-nav   li")
    eleTexts = [ele.text for ele in eles]
    actual = '|'.join(eleTexts)
    if actual == expected:
        print('app page pass')
    else:
        print('app page fail!!!!')




def checkVmail():
    expected = '''平板电脑|笔记本电脑|笔记本配件'''
    from selenium.webdriver.common.action_chains import ActionChains
    ac = ActionChains(driver)

    # 演示的时候，单步调试， 停在这里
    ac.move_to_element(driver.find_element_by_id('zxnav_1')).perform()

    # 用 setTimeout(function(){debugger;},3000) 来 查看元素
    # 分析 得知  zxnav_1 ，2,3,4  分别就是对应 菜单的，里面有隐藏菜单
    # eles = driver.find_elements_by_css_selector('#zxnav_1 .subcate-item a span')
    '#zxnav_1 div.category-item-bg a'
    eles=driver.find_elements_by_css_selector('#zxnav_1 div.category-item-bg a')
    eleTexts = [ele.text for ele in eles]
    actual = '|'.join(eleTexts)
    if actual == expected:
        print('main page pass')
    else:
        print('main page fail!!!!')
        print(actual)
        print(expected)


for handle in driver.window_handles:
    driver.switch_to.window(handle)

    if '消费者业务官网' in driver.title:
        checkHuaWei()
    # elif '应用市场' in driver.title:
    #     #     checkAppmarket()
    elif '华为商城（VMALL.COM）' in driver.title:
        checkVmail()


driver.quit()


