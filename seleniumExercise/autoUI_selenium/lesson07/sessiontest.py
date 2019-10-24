
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)


driver.get('http://localhost/mgr/ps/mgr/index.html#/')
driver.add_cookie({'name':'sessionid', 'value': '9tsldspykg0m1dr6scf56t4csxtxj3dw'})

driver.get('http://localhost/mgr/ps/mgr/index.html#/')

input('....press to quit....')

driver.quit()
