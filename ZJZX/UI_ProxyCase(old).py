#-*- coding:utf-8 -*-
# @Time  :2019/6/26 15:42
import time,random,requests
import win32com.client
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 登录
from selenium.webdriver.support.select import Select


def login(username='admin',password='123456'):
    driver.get(url)
    driver.find_element_by_css_selector('#UserName').send_keys(username)
    driver.find_element_by_css_selector('#Password').send_keys(password)
    driver.find_element_by_css_selector('.btns').click()

# 进入招标代理模块
def intoProxy():
    menuList = driver.find_elements_by_css_selector('ul.page-sidebar-menu>li')
    for one in menuList:
        if one.text == '招标代理':
            one.click()
            time.sleep(1)
            one.find_element_by_css_selector(
                '''a[onclick="tabNav.add('2021','招标代理业务','/Proxy/Proxy/ProxyIndex')"]''').click()
            break
    # 切换到工作区域frame
    indexframe = driver.find_element_by_css_selector('iframe[src="/Proxy/Proxy/ProxyIndex"]')
    driver.switch_to.frame(indexframe)
    time.sleep(1)

# 进行收件登记
def receiptToRegister():
    #进行收件登记编辑保存操作
    driver.find_element_by_css_selector('#table-list>thead a').click()
    driver.switch_to.alert.accept()
    time.sleep(1)
    driver.switch_to.frame(driver.find_element_by_css_selector('iframe[src="/Proxy/Proxy/PrProInfoAddOrEdit?IsHaveTCK=True"]'))
    driver.find_element_by_css_selector('#ProNo').send_keys(f'招标编号{random_num}')
    proname=f'招标代理tsh{random_num}'
    driver.find_element_by_css_selector('#ProName').send_keys(proname)
    driver.find_element_by_css_selector('#UnitName').send_keys(f'cx{random_num}')
    driver.find_element_by_css_selector('#ContactInformation').send_keys('15789789064')
    driver.find_element_by_css_selector('#TradingPlace').send_keys(f'cx{random_num}')
    driver.find_element_by_css_selector('#ProScale').send_keys(f'大{random_num}')
    #填写备注----------------------------------------------------------富文本编辑器中输入文本问题，暂未解决？？？？？？？？？？？？？？？？？？？？？？？？
    # driver.switch_to.frame(driver.find_element_by_css_selector(
    #     'iframe#ueditor_0'))
    # driver.execute_script("document.getElementsByTagName('p')[0].innerHTML='备注备注';")
    # driver.switch_to.parent_frame()
    # 上传附件----------------------------------------------------------由·于浏览器禁止运行flash，无法进行附件上传？？？？？？？？？？？？？？？？？？？？
    # driver.find_element_by_css_selector('.nav.nav-tabs>li:nth-child(2)').click()
    # driver.find_element_by_css_selector('#SWFUpload_0').click()
    # shell=win32com.client.Dispatch('WsScript.Shell')
    # shell.SendKeys(r'G:\常用测试素材\word文档测试.docx'+'\n')
    driver.find_element_by_css_selector('#form0 button:nth-child(1)').click()
    time.sleep(2)
    #重新点击进入项目，进行提交审核操作
    driver.switch_to.alert.accept()
    time.sleep(1)
    driver.switch_to.parent_frame()
    driver.switch_to.frame(driver.find_element_by_css_selector('iframe[src*="/Proxy/Proxy/PrProInfoAddOrEdit?IsHavePr=true&ProInfoID="]'))
    driver.find_element_by_css_selector('.row-fluid .span5:nth-child(2)>button[class="btn btn-warning"]').click()
    time.sleep(1)
    driver.find_element_by_css_selector('.modal.fade.in button.btn.btn-primary').click()
    print(f'已新建：{proname}')
    # 进行工作流审核工作
    # 选择最后一个审核人，判断样式
    time.sleep(2)
    driver.switch_to.frame(driver.find_element_by_css_selector('iframe[src="/Proxy/Proxy/ProxyIndex"]'))
    driver.switch_to.frame(
        driver.find_element_by_css_selector('iframe[src*="/Proxy/Proxy/PrProInfoAddOrEdit?IsHavePr=true&ProInfoID="]'))
    lastauditor = driver.find_element_by_css_selector(
        '.span8.offset2 table#table-list>tbody>tr:last-child>td:nth-child(2)>div')
    if lastauditor.get_attribute('class') == 'circle circle-warning':
        # 退出登录
        requests.get(f'{url}Systems/Home/LogOut')
    return proname, lastauditor

#进行合同签订,operationtype=1：代表选择已有合同，operationtype=2：代表新建合同
def contractsign(operationtype):
    driver.find_element_by_css_selector('#table-list>tbody>tr:nth-child(1)>td:nth-child(2)').click()
    time.sleep(1)
    driver.find_element_by_css_selector('button.btn.btn-danger').click()
    time.sleep(1)
    driver.switch_to.frame(driver.find_element_by_css_selector('iframe[src*="/Proxy/Proxy/PrContractSignAddOrEdit?IsHavePr=true&ProInfoID="]'))
    if operationtype==1:
        existingcontracts=driver.find_element_by_css_selector('#SelectContractSignID')
        if len(Select(existingcontracts).options)>1:
            Select(existingcontracts).select_by_index(0)
        else:
            choice=input('没有已有合同，请确认是否要新建合同：1.不要 2.要 ：\n')
            if choice=='2':
                driver.switch_to.parent_frame()
                contractsign(2)
            else:
                print('--------没有已有合同，且不进行新建合同操作，合同签订无法进行，测试结束--------')
                driver.quit()
    elif operationtype==2:
        driver.find_element_by_css_selector('div.span1 .btn.btn-default').click()
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(1)
        driver.find_element_by_css_selector('#ContractNO').send_keys(f'合同编号{random_num}')
        driver.find_element_by_css_selector('#ProNo').send_keys(f'招标编号{random_num}')
        driver.find_element_by_css_selector('#ContractName').send_keys(f'合同名称{random_num}')
        driver.find_element_by_css_selector('#ContractRange').send_keys(f'合同范围{random_num}')
        driver.find_element_by_css_selector('#LaunchSaveBtn').click()
        time.sleep(1)
        driver.find_element_by_css_selector('#modal_confirm button.btn.btn-primary').click()
        print(f'合同已新建：{proname}')
        # 进行工作流审核工作
        # 选择最后一个审核人，判断样式
        time.sleep(2)
        print(driver.page_source)
        driver.switch_to.frame(driver.find_element_by_css_selector('iframe[src="/Proxy/Proxy/ProxyIndex"]'))
        driver.switch_to.frame(
            driver.find_element_by_css_selector(
                'iframe[src*="/Proxy/Proxy/PrProInfoAddOrEdit?IsHavePr=true&ProInfoID="]'))
        lastauditor = driver.find_element_by_css_selector(
            '.span8.offset2 table#table-list>tbody>tr:last-child>td:nth-child(2)>div')
        if lastauditor.get_attribute('class') == 'circle circle-warning':
            # 退出登录
            requests.get(f'{url}Systems/Home/LogOut')

#工作流审核
def audit(proname,lastauditor):
    login(lastauditor.text.split())
    # 进入审核任务模块
    menuList = driver.find_elements_by_css_selector('ul.page-sidebar-menu>li')
    for one in menuList:
        if one.text == '审核任务':
            one.click()
            break
    driver.switch_to.frame(driver.find_element_by_css_selector('iframe[src="/WorkFlows/Instance/MyWorkFlow"]'))
    auditlist=driver.find_elements_by_css_selector('td:nth-child(2)>a')
    for one in auditlist:
        if proname in one.text:
            one.click()
            break
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    driver.find_element_by_css_selector('button.btn.btn-primary[onclick="onBefore()"]').click()
    time.sleep(1)
    driver.find_element_by_css_selector('button[type="submit"]').click()
    time.sleep(2)
    lastauditorlist = driver.find_elements_by_css_selector(
        '.span8.offset2 table#table-list>tbody>tr:last-child>td:nth-child(2)>div')
    if lastauditorlist[0].get_attribute('class') == 'circle circle-warning':
        # 退出登录
        requests.get(f'{url}Systems/Home/LogOut')
        audit(proname,lastauditorlist[0])
    else:
        print(f'已审核：{proname}')

driver=webdriver.Chrome(r'F:\selenium\driver\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
url='http://192.168.0.108:1606/'
#设置随机标识
rand = random.randint(1, 10000)
date = time.strftime("%m%d", time.localtime())
random_num=f'{rand}-{date}'
try:
    login()
    #进入招标代理模块
    intoProxy()
    #1、进行收件登记操作
    proname,lastauditor=receiptToRegister()
    audit(proname, lastauditor)
    #2、进行合同签订操作
    login()
    intoProxy()
    contractsign(1)

except Exception as e:
    driver.quit()
    print('--------------出错了----------------')
    raise e
time.sleep(3)
driver.quit()

