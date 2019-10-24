#-*- coding:utf-8 -*-
# @Time  :2019-08-14 17:51
import requests
from pprint import pprint
#------------------------登录操作
def login(username,password):
    head={
        "Host":"localhost:8080",
        "Content-Type":"application/x-www-form-urlencoded"
    }
    datas={
        "username":username,
        "password": password
    }
    loginResponse=requests.post('http://localhost:8080/api/mgr/loginReq', headers=head, data=datas)
    # print('登录返回：',loginResponse.json())
    return loginResponse.json(),loginResponse.cookies


#-------------------------列出课程
def list_course():
    loginRes, cookies = login('auto', 'sdfsdfsdf')
    assert loginRes['retcode'] == 0
    sessionid = cookies['sessionid']
    listResponse=requests.get('http://localhost:8080/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20',cookies={"sessionid":sessionid}).json()
    return [one['name'] for one in listResponse['retlist']]

