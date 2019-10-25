'''
本用例用于进行抽查完成操作
'''
from selenium import webdriver
import time
def findByCss(locator,isMulti=False):
    if isMulti==True:
        return driver.find_elements_by_css_selector(locator)
    return driver.find_element_by_css_selector(locator)
def login(username='admin',password='123456'):
    findByCss('#UserName').send_keys(username)
    findByCss('#Password').send_keys(password)
    findByCss('.btns').click()
    time.sleep(1)

def inAudit():
    findByCss('.row a[href="/Project/InAudit/InAudit"]').click()
    time.sleep(1)
    for one in range(1,100001):
        #修改按钮list
        multis=findByCss('''a[onclick*="Dialog.iframe('修改','/Project/InAudit/InAuditAddOrEdit/"]''',isMulti=True)
        #实际完成时间list
        realcompletes=findByCss('#table-list td:nth-child(8)',isMulti=True)
        if realcompletes[0].text!='':
            break
        multis[0].click()
        time.sleep(1)
        driver.switch_to.frame(findByCss('iframe[src*="/Project/InAudit/InAuditAddOrEdit/"]'))
        findByCss('button[onclick="ConfirmComplete()"]').click()
        time.sleep(1)
        findByCss('.modal-footer button.btn.btn-primary').click()
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(1)

driver=webdriver.Chrome()
driver.get('http://127.0.0.1:8082')
driver.implicitly_wait(10)
driver.maximize_window()
login()
inAudit()



