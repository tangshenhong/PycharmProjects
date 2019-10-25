#-*- coding:utf-8 -*-
# @Time  :2019/6/26 15:42
import time,random,requests
from selenium import webdriver
from selenium.webdriver.support.select import Select
def findByCss(locator,isMulti=False):
    if isMulti==True:
        return driver.find_elements_by_css_selector(locator)
    return driver.find_element_by_css_selector(locator)
# 登录
def login(username='admin',password='123456'):
    driver.get(url)
    findByCss('#UserName').send_keys(username)
    findByCss('#Password').send_keys(password)
    findByCss('.btns').click()

# 进入招标代理模块
def intoProxy():
    menuList = findByCss('ul.page-sidebar-menu>li',True)
    for one in menuList:
        if one.text == '招标工程任务':
            one.click()
            time.sleep(1)
            one.find_element_by_css_selector(
                '''a[onclick="tabNav.add('2330','项目招标','/Proxy/Proxy/Proxy')"]''').click()
            break
    # 切换到工作区域frame
    indexframe = findByCss('iframe[src="/Proxy/Proxy/Proxy"]')
    driver.switch_to.frame(indexframe)
    time.sleep(1)

# 进行收件登记
def receiptToRegister():
    # 进行收件登记编辑保存操作
    findByCss('a[href="/Proxy/Proxy/PrProInfoAddOrEdit?isNew=True"]').click()
    driver.switch_to.alert.accept()
    time.sleep(1)
    findByCss('#ProNo').clear()
    findByCss('#ProNo').send_keys(f'招标编号{time_sign}')
    proname=f'招标代理tsh{time_sign}'
    findByCss('#ProName').send_keys(proname)
    findByCss('#UnitName').send_keys(f'cx{time_sign}')
    findByCss('#ContactInformation').send_keys('15789789064')
    findByCss('#TradingPlace').send_keys(f'cx{time_sign}')
    findByCss('#ProScale').send_keys(f'大{time_sign}')
    #填写备注----------------------------------------------------------富文本编辑器中输入文本问题，暂未解决？？？？？？？？？？？？？？？？？？？？？？？？
    # driver.switch_to.frame(findByCss(
    #     'iframe#ueditor_0'))
    # driver.execute_script("document.getElementsByTagName('p')[0].innerHTML='备注备注';")
    # driver.switch_to.parent_frame()
    # 上传附件----------------------------------------------------------由·于浏览器禁止运行flash，无法进行附件上传？？？？？？？？？？？？？？？？？？？？
    # findByCss('.nav.nav-tabs>li:nth-child(2)').click()
    # findByCss('#SWFUpload_0').click()
    # shell=win32com.client.Dispatch('WsScript.Shell')
    # shell.SendKeys(r'G:\常用测试素材\word文档测试.docx'+'\n')
    findByCss('#form0 button:nth-child(1)').click()
    time.sleep(4)
    #重新点击进入项目，进行提交审核操作
    findByCss('#table-list>tbody>tr:nth-child(1)>td:nth-child(4) a').click()
    time.sleep(2)
    findByCss('div[panelindex="代理收件登记"]').click()
    driver.switch_to.alert.accept()
    driver.switch_to.frame(findByCss(
        'iframe[src*="/Proxy/Proxy/PrProInfoAddOrEdit?IsHavePr=true&ProInfoID="]'))
    findByCss('button[onclick="launch(true);"]').click()
    time.sleep(2)
    findByCss('.mt15.modal-open #modal_confirm .btn.btn-primary').click()
    print(f'已新建：{proname}')
    # 进行工作流审核工作
    # 选择最后一个审核人，判断样式
    time.sleep(2)
    driver.switch_to.frame(findByCss(
        'iframe[src*="/Proxy/Proxy/Proxy"]'))
    driver.switch_to.frame(findByCss(
        'iframe[src*="/Proxy/Proxy/PrProInfoAddOrEdit?IsHavePr=true&ProInfoID="]'))
    lastauditor = findByCss('.span8.offset2 table#table-list>tbody>tr:last-child>td:nth-child(2)>div')
    if lastauditor.get_attribute('class') == 'circle circle-warning':
        # 退出登录
        requests.get(f'{url}Systems/Home/LogOut')
    return proname, lastauditor

#进行合同签订,operationtype=1：代表选择已有合同，operationtype=2：代表新建合同
def contractsign(operationtype):
    findByCss('#table-list>tbody>tr:nth-child(1)>td:nth-child(4) a').click()
    time.sleep(1)
    findByCss('div[panelindex="代理合同签订"]').click()
    time.sleep(1)
    driver.switch_to.frame(findByCss('iframe[src*="/Proxy/Proxy/PrContractSignAddOrEdit?IsHavePr=true&ProInfoID="]'))
    if operationtype==1:
        existingcontracts=findByCss('#SelectContractSignID')
        options=Select(existingcontracts).options
        if len(options)>1:
            Select(existingcontracts).select_by_index(random.randint(1,len(options)))
            findByCss('#SaveBtn').click()
            time.sleep(1)
        else:
            choice=input('没有已有合同，请确认是否要新建合同：1.不要 2.要 ：\n')
            if choice=='2':
                driver.switch_to.parent_frame()
                contractsign(2)
            else:
                print('--------没有已有合同，且不进行新建合同操作，合同签订无法进行，测试结束--------')
                driver.quit()
    elif operationtype==2:
        findByCss('div.span1 .btn.btn-default').click()
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(1)
        findByCss('#ContractNO').send_keys(f'合同编号{time_sign}')
        findByCss('#ProNo').send_keys(f'招标编号{time_sign}')
        findByCss('#ContractName').send_keys(f'合同名称{time_sign}')
        findByCss('#ContractRange').send_keys(f'合同范围{time_sign}')
        findByCss('#LaunchSaveBtn').click()
        time.sleep(1)
        findByCss('#modal_confirm button.btn.btn-primary').click()
        # print(f'合同已新建：{proname}')
        # 进行工作流审核工作
        # 选择最后一个审核人，判断样式
        time.sleep(2)
        print(driver.page_source)
        driver.switch_to.frame(findByCss('iframe[src="/Proxy/Proxy/ProxyIndex"]'))
        driver.switch_to.frame(
            findByCss(
                'iframe[src*="/Proxy/Proxy/PrProInfoAddOrEdit?IsHavePr=true&ProInfoID="]'))
        lastauditor = findByCss(
            '.span8.offset2 table#table-list>tbody>tr:last-child>td:nth-child(2)>div')
        if lastauditor.get_attribute('class') == 'circle circle-warning':
            # 退出登录
            requests.get(f'{url}Systems/Home/LogOut')

#工作流审核
def audit(proname,lastauditor):
    login(lastauditor.text.split())
    # 进入审核任务模块
    menuList = findByCss('ul.page-sidebar-menu>li',True)
    for one in menuList:
        if one.text == '审核任务':
            one.click()
            break
    driver.switch_to.frame(findByCss('iframe[src="/WorkFlows/Instance/MyWorkFlow"]'))
    time.sleep(1)
    auditlist=findByCss('td:nth-child(2)>a',True)
    for one in auditlist:
        if proname in one.text:
            one.click()
            break
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    findByCss('button.btn.btn-primary[onclick="onBefore()"]').click()
    time.sleep(2)
    findByCss('button[type="submit"]').click()
    time.sleep(2)
    lastauditorlist = findByCss(
        '.span8.offset2 table#table-list>tbody>tr:last-child>td:nth-child(2)>div',True)
    if lastauditorlist[0].get_attribute('class') == 'circle circle-warning':
        # 退出登录
        requests.get(f'{url}Systems/Home/LogOut')
        audit(proname,lastauditorlist[0])
    else:
        print(f'已审核：{proname}')

driver=webdriver.Chrome(r'F:\selenium\driver\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
url='http://127.0.0.1:8081'

try:
    # 设置唯一时间标识
    time_sign = time.strftime("%m%d_%H%M_%S", time.localtime())
    login()
    # 进入新版招标代理模块
    intoProxy()
    # 1、进行收件登记操作
    proname, lastauditor = receiptToRegister()
    audit(proname, lastauditor)
    # # 2、进行合同签订操作
    # login()
    # intoProxy()
    # contractsign(1)


except Exception as e:
    # driver.quit()
    print('--------------出错了----------------')
    raise e
time.sleep(3)
driver.quit()

