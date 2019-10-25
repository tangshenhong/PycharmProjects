from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
class WebOpAdmin():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        self.driver=driver
    def findByCss(self,locator,isMulti=False):
        if isMulti==True:
            return self.driver.find_elements_by_css_selector(locator)
        return self.driver.find_element_by_css_selector(locator)
    def setupWebTest(self,url):
        self.driver.get(url)
    def tearDownWebTest(self):
        self.driver.quit()
    def loginWebSite(self, username, passwd):
        self.findByCss('#username').send_keys(username)
        self.findByCss('#password').send_keys(passwd)
        self.findByCss('button[onclick="postLoginRequest()"]').click()
        time.sleep(1)
#课程管理库
    def DeleteAllCourse(self):
        time.sleep(1)
        self.driver.implicitly_wait(2)
        self.findByCss('a[ui-sref="course"]').click()
        while True:
            time.sleep(1)
            deles = self.findByCss('[ng-click="delOne(one)"]',True)
            if deles==[]:
                break
            deles[0].click()
            self.findByCss('.btn.btn-primary').click()
        self.driver.implicitly_wait(10)
    def AddCourse(self, name, desc, idx):
        time.sleep(1)
        self.findByCss('button[ng-click="showAddOne=true"]').click()
        time.sleep(1)
        nameEle=self.findByCss('[ng-model="addData.name"]')
        nameEle.clear()
        nameEle.send_keys(name)
        descEle=self.findByCss('[ng-model="addData.desc"]')
        descEle.clear()
        descEle.send_keys(desc)
        idxEle=self.findByCss('[ng-model="addData.display_idx"]')
        idxEle.clear()
        idxEle.send_keys(idx)
        self.findByCss('[ng-click="addOne()"]').click()
    def checkCourse(self,expectCourses):
        reals=self.findByCss('tr>td:nth-child(2)',True)
        realCourses=[]
        for one in reals:
            realCourses.append(one.text)
        assert expectCourses==realCourses
#教师管理库
    def DeleteAllTeacher(self):
        time.sleep(1)
        self.driver.implicitly_wait(2)
        self.findByCss('a[href="#/teacher"]').click()
        while True:
            time.sleep(1)
            deles = self.findByCss('button[ng-click="delOne(one)"]', isMulti=True)
            if deles==[]:
                break
            deles[0].click()
            self.findByCss('button.btn.btn-primary').click()
        self.driver.implicitly_wait(10)

    def AddTeacher(self,realname,username,desc,idx,courseName):
        time.sleep(1)
        self.findByCss('a[href="#/teacher"]').click()
        self.findByCss('button[ng-click="showAddOne=true"]').click()
        realnameEle=self.findByCss('input[ng-model="addEditData.realname"]')
        realnameEle.clear()
        realnameEle.send_keys(realname)
        usernameEle=self.findByCss('input[ng-model="addEditData.username"]')
        usernameEle.clear()
        usernameEle.send_keys(username)
        descEle=self.findByCss('textarea[ng-model="addEditData.desc"]')
        descEle.clear()
        descEle.send_keys(desc)
        idxEle=self.findByCss('input[ng-model="addEditData.display_idx"]')
        idxEle.clear()
        idxEle.send_keys(idx)
        courseSelect=self.findByCss('[ng-model="$parent.courseSelected"]')
        Select(courseSelect).select_by_visible_text(courseName)
        self.findByCss('button[ng-click="addOne()"]').click()
    def checkTeacher(self,expectTeachers):
        teachers=self.findByCss('tr  td:nth-child(2) span[ng-if="!one.editing"]',isMulti=True)
        teacherNames=[]
        for one in teachers:
            teacherNames.append(one.text)
        assert teacherNames==expectTeachers

# 培训班管理库
    def DeleteTrainingClass(self):
        self.driver.implicitly_wait(2)
        self.findByCss('a[href="#/training"]').click()
        while True:
            time.sleep(1)
            deles=self.findByCss('button[ng-click="delOne(one)"]',isMulti=True)
            if deles==[]:
                break
            deles[0].click()
            time.sleep(1)
            self.findByCss('button.btn.btn-primary').click()
        self.driver.implicitly_wait(10)

    def AddTrainingClass(self,name,desc,idx,courses):
        time.sleep(1)
        self.findByCss('a[href="#/training"]').click()
        time.sleep(1)
        self.findByCss('button[ng-click="showAddOne=true"]').click()
        time.sleep(1)
        self.findByCss('input[ng-model="addEditData.name"]').send_keys(name)
        self.findByCss('textarea[ng-model="addEditData.desc"]').send_keys(desc)
        idxEle=self.findByCss('input[ng-model="addEditData.display_idx"]')
        idxEle.clear()
        idxEle.send_keys(idx)
        selectCourse = self.findByCss('select[ng-model="$parent.courseSelected"]')
        for one in courses:
            Select(selectCourse).select_by_visible_text(one)
            self.findByCss('button[ng-click="addEditData.addTeachCourse()"]').click()
            time.sleep(1)
        self.findByCss('button[ng-click="addOne()"]').click()

    def checkTrainingClass(self, expectTrainingClass):
        time.sleep(1)
        trainingClassEle=self.findByCss('td:nth-child(2)',isMulti=True)
        trainingClasses=[]
        for one in trainingClassEle:
            trainingClasses.append(one.text)
        assert expectTrainingClass==trainingClasses
# 培训班期管理库
    def DeleteTrainingClassPeriod(self):
        self.driver.implicitly_wait(2)
        self.findByCss('a[href="#/traininggrade"]').click()
        while True:
            time.sleep(1)
            deles=self.findByCss('button[ng-click="delOne(one)"]',isMulti=True)
            if deles==[]:
                break
            deles[0].click()
            time.sleep(1)
            self.findByCss('button.btn.btn-primary').click()
        self.driver.implicitly_wait(10)

    def AddTrainingClassPeriod(self,name,desc,idx,trainingClass):
        time.sleep(1)
        self.findByCss('a[href="#/traininggrade"]').click()
        time.sleep(1)
        self.findByCss('button[ng-click="showAddOne=true"]').click()
        time.sleep(1)
        self.findByCss('input[ng-model="addEditData.name"]').send_keys(name)
        self.findByCss('textarea[ng-model="addEditData.desc"]').send_keys(desc)
        idxEle=self.findByCss('input[ng-model="addEditData.display_idx"]')
        idxEle.clear()
        idxEle.send_keys(idx)
        selectCourse = self.findByCss('select[ng-model="$parent.addEditData.training_id"]')
        Select(selectCourse).select_by_visible_text(trainingClass)
        time.sleep(1)
        self.findByCss('button[ng-click="addOne()"]').click()

    def checkTrainingClassPeriod(self, expectTrainingClassPeriod):
        time.sleep(1)
        trainingClassPeriodEle=self.findByCss('td:nth-child(2)',isMulti=True)
        trainingClassePeriods=[]
        for one in trainingClassPeriodEle:
            trainingClassePeriods.append(one.text)
        assert expectTrainingClassPeriod==trainingClassePeriods
# obj=WebOpAdmin()
# obj.setupWebTest('http://localhost/mgr/login/login.html')
# obj.loginWebSite('auto','sdfsdfsdf')
# obj.AddTeacher('test','test','test',1,'初中语文')
# obj.DeleteAllCourse()
# obj.AddCourse('测试2','描述描述',2)