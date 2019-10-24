from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get('http://localhost/mgr/login/login.html')

driver.find_element_by_id('username').send_keys('auto')
driver.find_element_by_id('password').send_keys('sdfsdfsdf')

driver.find_element_by_tag_name('button').click()


def addCourse(driver, name, desc, idx):

    driver.find_element_by_css_selector("a[ui-sref='course']").click()
    time.sleep(1)

    driver.find_element_by_css_selector(
        'button[ng-click^=showAddOne]').click()

    ele = driver.find_element_by_css_selector(
        "input[ng-model='addData.name']")
    ele.clear()
    ele.send_keys(name)

    ele = driver.find_element_by_css_selector(
        "textarea[ng-model='addData.desc']")
    ele.clear()
    ele.send_keys(desc)

    ele = driver.find_element_by_css_selector("input[ng-model='addData.display_idx']")
    ele.clear()
    ele.send_keys(idx)

    driver.find_element_by_css_selector('button[ng-click^=addOne]').click()


def DeleteAllCourse(driver):
    driver.implicitly_wait(2)
    while 1:
        delButtons = driver.find_elements_by_css_selector(
            '*[ng-click^=delOne]')
        if delButtons==[]:
            break
        delButtons[0].click()
        driver.find_element_by_css_selector(
            '.btn-primary').click()
        time.sleep(1)

# driver.implicitly_wait(10)

DeleteAllCourse(driver)
time.sleep(1)
addCourse(driver, '数学', '数学', 1)
addCourse(driver, '语文', '语文', 2)

time.sleep(1)
DeleteAllCourse(driver)

driver.quit()
