#-*- coding:utf-8 -*-
# @Time  :2019/7/3 10:08
"""
本用例用于造价编审业务模块测试
"""
import time,datetime
from random import randint
from selenium import webdriver
from selenium.webdriver.support.select import Select
class MyTasks():
    #工具方法：通过locator定位元素
    def findByCss(self,locator,isMulti=False):
        """
        :param locator:定位器
        :param isMulti: 是否定位多元素
        """
        if isMulti==True:
            return driver.find_elements_by_css_selector(locator)
        return driver.find_element_by_css_selector(locator)
    # ------登录
    def login(self,username='admin',password='123456'):
        driver.get(url)
        self.findByCss('#UserName').send_keys(username)
        self.findByCss('#Password').send_keys(password)
        self.findByCss('.btns').click()
    # ------进入造价编审模块
    def intoMyTasks(self,proname=''):
        menuList = self.findByCss('ul.page-sidebar-menu>li',True)
        for one in menuList:
            if one.text == '造价管理':
                one.click()
                time.sleep(1)
                one.find_element_by_css_selector(
                    '''a[onclick="tabNav.add('1878','造价业务编审','/Project/AssignMission/MyTasks')"]''').click()
                break
        # 切换到工作区域frame
        time.sleep(1)
        indexframe = self.findByCss('iframe[src="/Project/AssignMission/MyTasks"]')
        driver.switch_to.frame(indexframe)
        time.sleep(1)
        #若传入proname，则进入具体项目详情页
        if proname!='':
            self.findByCss('a.btn.btn-danger[href="/Project/AssignMission/MyTasks"]')
            pronames = self.findByCss('a[href*="/Project/AssignMission/MyTasksDetail?ProInfoID"]', True)
            for one in pronames:
                if one.text.split()[0] == proname:
                    one.click()
                    time.sleep(1)
                    break

    #------收件登记
    def ProInfoOrders(self):
        self.login()
        self.intoMyTasks()
        #点击进行收件登记
        self.findByCss('a[onclick="OrderProInfo()"]').click()
        time.sleep(3)
        driver.switch_to.alert.accept()
        #项目名称
        proname = f'造价编审tsh{rand}'
        self.findByCss('#ProName').send_keys(proname)
        #项目编号
        referenceClass=self.findByCss('select#ReferenceClass')
        Select(referenceClass).select_by_index(randint(1,len(Select(referenceClass).options)-1))
        #咨询类别
        consultingClass=self.findByCss('#ConsultingClassID')
        Select(consultingClass).select_by_index(randint(0,len(Select(consultingClass).options)-1))
        #委托单位
        self.findByCss('#select2-DelegateCustomerInfoID-container').click()
        time.sleep(1)
        delegateCustomers=self.findByCss('ul#select2-DelegateCustomerInfoID-results>li',True)
        delegateCustomers[randint(0,len(delegateCustomers)-1)].click()
        #送审金额
        auditAmount=self.findByCss('#AuditAmount')
        auditAmount.clear()
        auditAmount.send_keys(randint(5000,8000))
        #业务来源
        self.findByCss('#BusinessSources').send_keys(f'唐XX')
        #所选专业
        SpecialtyClass=self.findByCss('#SpecialtyClassID')
        Select(SpecialtyClass).select_by_index(randint(0, len(Select(SpecialtyClass).options) - 1))
        #所属部门
        self.findByCss('#select2-DepartmentID-container').click()
        time.sleep(2)
        departments=self.findByCss('#select2-DepartmentID-results>li',True)
        departments[randint(0,len(departments)-1)].click()
        #项目开始、结束时间
        begintime = datetime.datetime.now().strftime('%Y-%m-%d')
        offset = datetime.timedelta(days=30)
        endtime=(datetime.datetime.now() + offset).strftime('%Y-%m-%d')
        self.findByCss('#ProBeginTime').send_keys(begintime)
        self.findByCss('#ProEndTime').send_keys(endtime)
        #备注
        self.findByCss('#Remark').send_keys('备注test')
        #清单列表
        dataListing=self.findByCss('#dataListing')
        Select(dataListing).select_by_index(randint(1,len(Select(dataListing).options)-1))
        #清单列表有时有数据，有时没有，需要考虑到！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        # self.findByCss('input[name="Number"]').send_keys('5')
        # self.findByCss('input[name = "PageNumber"]').send_keys('50')
        # self.findByCss('#table-datalisting input[name="Remark"]').send_keys('清单列表的备注')
        #保存
        self.findByCss('button[onclick="draftOrSubmit(false);"]').click()
        time.sleep(1)
        self.findByCss('a[href="/Project/AssignMission/MyTasks?qType=3"]').click()
        time.sleep(2)
        self.findByCss('#table-list>tbody>tr:nth-child(1)>td[name="1"]>a').click()
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(2)
        self.findByCss('button[onclick="draftOrSubmit(true)"]').click()
        time.sleep(1)
        self.findByCss('#modal_confirm .btn.btn-primary').click()
        time.sleep(1)
        print(f'已新建项目：{proname}')
        #查看下一步审核人员
        self.findByCss('.table.table-condensed.table-hover>tbody>tr>td:nth-child(2)>a').click()
        time.sleep(2)
        lastauditor = self.findByCss(
            '.span8.offset2 table#table-list>tbody>tr:last-child>td:nth-child(2)>div')
        if lastauditor.get_attribute('class') == 'circle circle-warning':
            #进行收件登记审核
            self.ordersAudit(proname,lastauditor.text.split())
        return proname

    #------收件登记审核
    def ordersAudit(self,proname,lastauditor):
        """
        :param proname:项目名称
        :param lastauditor: 下一位审核人员
        :return:
        """
        time.sleep(1)
        self.login(lastauditor)
        # 进入审核任务模块
        menuList = self.findByCss('ul.page-sidebar-menu>li',True)
        for one in menuList:
            if one.text == '审核任务':
                one.click()
                time.sleep(1)
                break
        driver.switch_to.frame(self.findByCss('iframe[src="/WorkFlows/Instance/MyWorkFlow"]'))
        auditlist=self.findByCss('#div-list tbody>tr:nth-child(1)>td:nth-child(2)>a',True)
        for one in auditlist:
            if proname in one.text:
                one.click()
                time.sleep(4)
                break
        #选择项目负责人
        self.findByCss('#select2-ProjectLeaderUserID-container').click()
        time.sleep(2)
        persons=self.findByCss('#select2-ProjectLeaderUserID-results>li',isMulti=True)
        for one in persons:
            if one.text=='超级管理员':
                one.click()
        time.sleep(2)
        #选择项目模板
        project_template=self.findByCss('select#tempSelect')
        # Select(project_template).select_by_visible_text('预算审核模板')
        Select(project_template).select_by_visible_text('顺健项目模板')
        time.sleep(1)
        #批量设置任务负责人
        self.findByCss('#select2-ddlResponse-container').click()
        time.sleep(2)
        persons=self.findByCss('#select2-ddlResponse-results>li',isMulti=True)
        for on in persons:
            if one.text=='超级管理员':
                one.click()
        time.sleep(2)
        #进行保存、审核
        self.findByCss('.span8 button.btn.btn-primary').click()
        time.sleep(4)
        self.findByCss('.span10 button.btn.btn-primary').click()
        time.sleep(3)
        lastauditorlist = self.findByCss(
            '.span8.offset2 table#table-list>tbody>tr:last-child>td:nth-child(2)>div',True)
        if lastauditorlist[0].get_attribute('class') == 'circle circle-warning':
            self.ordersAudit(proname,lastauditorlist[0].text.split())
        else:
            print('已收件审核')
    #------合同签订
    def SignContract(self,proname,contractType=1):
        """
        :param proname:项目名称
        :param contractType: 合同类别，其中选择1：已有合同  2：新建合同  3：无合同
        """
        self.login()
        self.intoMyTasks(proname)
        self.findByCss('.btn-group.btn-group-sm>a:nth-child(3)').click()
        time.sleep(1)
        #切换到合同签订页面
        driver.switch_to.default_content()
        self.findByCss('a[href="#1988"]').click()
        driver.switch_to.frame(self.findByCss('iframe[src*="/Project/Orders/SignContractAddOrEdit?IsHavePr=true&ProInfoID="]'))
        time.sleep(1)
        if contractType==1: #选择已有合同
            selectContractSign=self.findByCss('#SelectContractSignID')
            if len(Select(selectContractSign).options)==1:
                print('不存在已有合同，请新建合同')
            else:
                Select(selectContractSign).select_by_index(randint(0,len(Select(selectContractSign).options)-1))
                time.sleep(1)
                self.findByCss('#SaveBtn').click()
                print('已选择已有合同')
                time.sleep(3)
                # 关闭合同签订页面
                driver.switch_to.default_content()
                self.findByCss('.active span[class="badge"]').click()
                time.sleep(1)
                driver.switch_to.frame(self.findByCss('iframe[src="/Project/AssignMission/MyTasks"]'))
        elif contractType==2: #新建合同
            self.findByCss('button[onclick="CreatContract()"]').click()
            time.sleep(1)
            driver.switch_to.alert.accept()
            #填写合同内容
            self.findByCss('#ContractNo').send_keys(rand)
            self.findByCss('#title').send_keys(f"{rand}的合同名称")
            self.findByCss('#ChargingBase').send_keys(f"{rand}的收费标准")
            #合同内容、备注为富文本编辑器，暂不做
            self.findByCss('#SaveBtn').click()
            time.sleep(2)
            driver.switch_to.alert.accept()
            time.sleep(1)
            self.findByCss('#LaunchSaveBtn').click()
            time.sleep(1)
            self.findByCss('#modal_confirm .btn.btn-primary').click()
            print('已新建合同')
            time.sleep(1)
            lastauditorlist = self.findByCss(
                '.span8.offset2 table#table-list>tbody>tr:last-child>td:nth-child(2)>div', True)
            if lastauditorlist[0].get_attribute('class') == 'circle circle-warning':
                self.audit(f"{rand}的合同名称", lastauditorlist[0].text.split(),'合同签订')
            #合同审核完成后，再次进入项目详情页
            self.login()
            self.intoMyTasks(proname)
        elif contractType==3: #项目无合同
            self.findByCss('button[onclick="emptyContract()"]').click()
            time.sleep(1)
            print('项目无合同')
            # 关闭合同签订页面
            driver.switch_to.default_content()
            self.findByCss('.active span[class="badge"]').click()
            time.sleep(1)
            driver.switch_to.frame(self.findByCss('iframe[src="/Project/AssignMission/MyTasks"]'))
    #------任务分配
    def taskAllocation(self,proname):
        time.sleep(1)
        self.findByCss('div[panelindex="任务分配"]').click()
        driver.switch_to.frame(self.findByCss('iframe[src*="/Project/AssignMission/TaskAllocationAddOrEdit?IsHavePr=true&ProInfoID="]'))
        self.findByCss('button[onclick="add()"]')
        #填写任务表单
        self.findByCss('input[name="UnitEngineeringName"]').send_keys('单位工程一')
        #负责人
        self.findByCss('#select2-AuditUserID-4u-container').click()
        time.sleep(1)
        self.findByCss('#select2-AuditUserID-4u-results',isMulti=True)[0].click()
        #计划时间
        self.findByCss('input[name="RequirementsEngTime"]').send_keys(datetime.datetime.now().strftime('%Y-%m-%d'))
        #成员
        self.findByCss("a[onclick='addPerson(1499)']").click()
        time.sleep(1)
        self.findByCss('#select2-CompileUserID-o0-container').click()
        time.sleep(1)
        member=self.findByCss('#select2-CompileUserID-o0-results', isMulti=True)[0]
        member.click()
        self.findByCss('#divContainer .btn.btn-warning').click()
        self.proWOrkSubmit(member,proname)
    #------项目编制
    #—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    def proWOrkSubmit(self,member,proname):
        self.login(member)
        self.intoMyTasks(proname)
        self.findByCss('div[panelindex="项目编制"]').click()
        time.sleep(1)
        self.findByCss('input[name="Cost"]').send_keys('30000元')
        self.findByCss('input[name="Remark"]').send_keys('单位工程一的备注')

    #进行通用审核
    def audit(self,auditname,lastauditor,task=''):
        """
        :param auditname:审核任务名称关键字
        :param lastauditor:最后一位审核人员
        :param task:当前任务类型
        """
        time.sleep(1)
        self.login(lastauditor)
        # 进入审核任务模块
        menuList = self.findByCss('ul.page-sidebar-menu>li', True)
        for one in menuList:
            if one.text == '审核任务':
                one.click()
                time.sleep(1)
                break
        driver.switch_to.frame(self.findByCss('iframe[src="/WorkFlows/Instance/MyWorkFlow"]'))
        auditlist = self.findByCss('#div-list tbody td:nth-child(2)>a', True)
        for one in auditlist:
            if auditname in one.text:
                one.click()
                time.sleep(1)
                break
        driver.implicitly_wait(2)
        #判断审核前，是否有编辑页面
        edit=self.findByCss('button[onclick="onBefore()"]',True)
        if edit!=[]:
            edit[0].click()
            time.sleep(1)
        self.findByCss('button[onclick="return OnBefore();"]').click()
        time.sleep(3)
        lastauditorlist = self.findByCss(
            '.span8.offset2 table#table-list>tbody>tr:last-child>td:nth-child(2)>div', True)
        if lastauditorlist[0].get_attribute('class') == 'circle circle-warning':
            self.audit(auditname, lastauditorlist[0].text.split(), '合同签订')
        driver.implicitly_wait(10)


driver=webdriver.Chrome(r'F:\selenium\driver\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
url='http://114.116.190.244:3040'
rand = time.strftime("%m%d_%H%M_%S", time.localtime())
try:
    mytasks=MyTasks()
    # 进行收件登记、审核操作
    proname=mytasks.ProInfoOrders()
    #进行合同签订操作
    mytasks.SignContract(proname,contractType=2)
    # #任务分配操作
    # mytasks.taskAllocation(proname)



except Exception as e:
    # driver.quit()
    print('--------------出错了----------------')
    raise e
time.sleep(3)
driver.quit()

