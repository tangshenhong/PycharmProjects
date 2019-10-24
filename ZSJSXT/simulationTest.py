#本用例用于模拟前台考试
import requests,time
from random import randint
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待
# 设置等待执行语句
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#根据css选择元素
def by_css(csstag,isMulti=False):
    if isMulti is False:
        return driver.find_element_by_css_selector(csstag)
    return driver.find_elements_by_css_selector(csstag)
# 登录
def login(url,username,password='123456'):
    driver.get(url)
    by_css('#UserName').send_keys(username)
    by_css('#Password').send_keys(password)
    # print('请输入验证码!!!!!!!')
    # time.sleep(5)
    by_css('.btns').click()

driver=webdriver.Chrome(r'F:\selenium\driver\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
url_backstage='http://127.0.0.1:8084/'
front_desk='http://127.0.0.1:8084/Web/Personnel/PersonnelLogin'
try:
    #进行考生安排
    login(url_backstage,'admin')
    by_css('a[href="/CXB/KC/Index"]').click()
    by_css('a[href="/CXB/KC/KCPersonnel"]').click()
    by_css('''a[onclick*="Dialog.iframe('考生安排'"]''').click()
    time.sleep(1)
    driver.switch_to.frame(by_css('iframe[src="/CXB/KC/KCPersonnelAddOrEdit"]'))
    by_css('#select2-Kcid-container').click()
    time.sleep(2)
    by_css('#select2-Kcid-results li:nth-child(3)').click()
    time.sleep(1)
    #--勾选前60个考生
    checkList=by_css('tbody>tr:nth-child(-n+60) input',isMulti=True)
    for one in checkList:
        one.click()
    #--将前60个考生的姓名存起来
    nameList=by_css('tbody>tr:nth-child(-n+60) [data-type="trueName"]',isMulti=True)
    names=[]
    for one in nameList:
        names.append(one.text)
    time.sleep(2)
    by_css('[onclick="submitData()"]').click()
    #进行前台考试
    for index,name in enumerate(names):
        login(front_desk,name)
        print(f'第{index+1}位：  {name}  开始考试')
        subjectDivs=by_css('[name="SubjectDiv"]',isMulti=True)
        for one in subjectDivs:
            commitButton=one.find_element_by_css_selector('''[onclick*="SaveAnnwer(this,"]''')
            if commitButton.get_attribute('class')=='btn btn-danger btn-xs':
                continue
            WebDriverWait(one, 10).until(
            EC.element_to_be_clickable(
            (By.CSS_SELECTOR,'''input[id*='Answer']''')))
            inputs=one.find_elements_by_css_selector("input[id*='Answer']")
            if len(inputs)==1:
                inputs[0].send_keys('填空测试')
            else:
                num=randint(0, len(inputs)-1)
                inputs[randint(0, num)].click()
            commitButton.click()
            time.sleep(7)
        # by_css('[onclick="QuitTest()"]').click()
        # time.sleep(2)
        # by_css('.btn.btn-primary').click()
    time.sleep(1)
except Exception as e:
    driver.quit()
    print('--------------出错了----------------')
    raise e
time.sleep(3)
driver.quit()

