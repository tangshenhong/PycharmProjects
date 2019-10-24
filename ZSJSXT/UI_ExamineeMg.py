#-*- coding:utf-8 -*-
# @Time  :2019/7/3 10:08
import requests,time
import datetime
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
#根据css选择元素
def by_css(csstag,isMulti=False):
    if isMulti is False:
        return driver.find_element_by_css_selector(csstag)
    return driver.find_elements_by_css_selector(csstag)
# 登录
def login(username,password='123456'):
    driver.get(url)
    by_css('#UserName').send_keys(username)
    by_css('#Password').send_keys(password)
    by_css('.btns').click()
#添加院校
def addSigSchool():
    by_css('.row  .col-md-1.col-xs-4.service-box:nth-child(3)').click()
    time.sleep(1)
    by_css('a[href="/CXB/SigTeam/SigSchool"]').click()
    time.sleep(1)
    by_css('''a[onclick="Dialog.iframe('添加院校','/CXB/SigTeam/SigSchoolAddOrEdit')"]''').click()
    driver.switch_to.frame(by_css('iframe[src="/CXB/SigTeam/SigSchoolAddOrEdit"]'))
    time.sleep(1)
    rand=randint(1,1000)
    by_css('#SchoolNO').send_keys(f'001XCXC-{rand}')
    by_css('#SchoolName').send_keys(f'院校-{rand}')
    #选择归属省份
    provinces=by_css('#province option',isMulti=True)
    Select(by_css('#province')).select_by_index(randint(1,len(provinces)-1))
    time.sleep(1)
    citys=by_css('#City option',isMulti=True)
    Select(by_css('#City')).select_by_index(randint(1,len(citys)-1))
    time.sleep(1)
    cityareas=by_css('#CityArea option',isMulti=True)
    if len(cityareas)>1:
        Select(by_css('#CityArea')).select_by_index(randint(1,len(cityareas)-1))
    #院校地址
    by_css('#SchoolAddress').send_keys(f'XX省XX市XX区-{rand}')
    schoolclass=by_css('#ClassID option',isMulti=True)
    Select(by_css('#ClassID')).select_by_index(randint(1,len(schoolclass)-1))
    time.sleep(1)
    by_css('#form0 button.btn.btn-primary').click()
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(1)
#添加团队
def addTeam():
    by_css('.row  .col-md-1.col-xs-4.service-box:nth-child(3)').click()
    time.sleep(1)
    by_css('a[href="/CXB/SigTeam/SigTeam"]').click()
    time.sleep(1)
    by_css('''a[onclick="Dialog.iframe('添加团队','/CXB/SigTeam/SigTeamAddOrEdit')"]''').click()
    time.sleep(1)
    driver.switch_to.frame(by_css('iframe[src="/CXB/SigTeam/SigTeamAddOrEdit"]'))
    time.sleep(1)
    schools=by_css('#SchoolID option',isMulti=True)
    Select(by_css('#SchoolID')).select_by_index(randint(1,len(schools)-1))
    time.sleep(1)
    rand = randint(1, 1000)
    by_css('#TeamName').send_keys(f'团队名称{rand}')
    by_css('#TeamSlogan').send_keys(f'团队口号{rand}')
    by_css('#form0 button.btn.btn-primary').click()
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(1)

#添加人员
def addExaminee():
    by_css('.row  .col-md-1.col-xs-4.service-box:nth-child(3)').click()
    time.sleep(1)
    by_css('a[href="/CXB/SigTeam/SigTeamPersonnel"]').click()
    time.sleep(1)
    by_css('''a[onclick="Dialog.iframe('添加团队人员','/CXB/SigTeam/SigTeamPersonnelAddOrEdit')"]''').click()
    time.sleep(1)
    driver.switch_to.frame(by_css('iframe[src="/CXB/SigTeam/SigTeamPersonnelAddOrEdit"]'))
    time.sleep(1)
    rand = randint(1, 1000)
    by_css('#TrueName').send_keys(f'人员{rand}')
    by_css('#PersonnelNO').send_keys(f'KSBM{rand}')
    schools=by_css('#SchoolID option',isMulti=True)
    Select(by_css('#SchoolID')).select_by_index(randint(1,len(schools)-1))
    teams=by_css('#TeamID option',isMulti=True)
    Select(by_css('#TeamID')).select_by_index(randint(1,len(teams)-1))
    teamroles=by_css('#TeamRole option',isMulti=True)
    Select(by_css('#TeamRole')).select_by_index(randint(1,len(teamroles)-1))
    by_css('#Professional').send_keys(f'专业{rand}')
    by_css('#Phone').send_keys(f'联系电话{rand}')
    by_css('#Email').send_keys(f'电子邮箱{rand}')
    by_css('#IdCard').send_keys(f'身份证号{rand}')
    by_css('#form0 button.btn.btn-primary').click()
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(1)


driver=webdriver.Chrome(r'F:\selenium\driver\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
url='http://192.168.0.108:1808/'
try:
    login('admin')
    for one in range(1,3):
        # addSigSchool()
        # addTeam()
        addExaminee()

except Exception as e:
    driver.quit()
    print('--------------出错了----------------')
    raise e
time.sleep(3)
driver.quit()

