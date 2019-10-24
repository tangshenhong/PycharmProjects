'''
本用例用于进行“外审转内审”操作
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

def turnInAudit():
    findByCss('a[href="/Project/OutAudit/OutAudit"]').click()
    time.sleep(1)
    for one in range(1,1000):
        time.sleep(2)
        outAudits = findByCss('#table-list tr>td:nth-child(2)', isMulti=True)
        if outAudits == []:
            break
        #全选
        findByCss('''input[onclick="CheckBox.selectAll('input.choose', this.checked)"]''').click()
        findByCss('button[onclick="TurnAudit()"]').click()
        time.sleep(1)
        findByCss('.modal-footer .btn.btn-primary').click()
        time.sleep(3)
        findByCss('a[href="/Project/OutAudit/OutAudit"]').click()

driver=webdriver.Chrome()
driver.get('http://127.0.0.1:8082')
driver.implicitly_wait(10)
driver.maximize_window()
login()
turnInAudit()


