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
    print('登录返回：',loginResponse.json())
    return loginResponse.json(),loginResponse.cookies

# -----------------------添加一门课程（系统中不存在、系统中已存在）
def add_course(name,desc,display_idx,sessionid):
    courseData={
        "action":"add_course",
        "data":'''{
      "name":"%s",
      "desc":"%s",
      "display_idx":"%s"
    } '''%(name,desc,display_idx)
    }
    head={
        "Content-Type":"application/x-www-form-urlencoded"
    }
    addRespsonse=requests.post('http://localhost:8080/api/mgr/sq_mgr/',headers=head, data=courseData,cookies={"sessionid":sessionid})
    print('添加课程返回：',addRespsonse.json())
    return addRespsonse.json()
#-------------------------列出课程
def list_course(sessionid):
    listResponse=requests.get('http://localhost:8080/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20',cookies={"sessionid":sessionid})
    print('列出课程返回：')
    pprint(listResponse.json())
    return listResponse.json()

# -------------------------修改课程
def update_course(id,name,desc,display_idx,sessionid):
    updateData={
        "action":"modify_course",
        "id":"%s"%id,
        "newdata":'''{
          "name":"%s",
          "desc":"%s",
          "display_idx":"%s"
        }'''%(name,desc,display_idx)
    }
    head={
        "Content-Type": "application/x-www-form-urlencoded"
    }
    updateResponse=requests.put('http://localhost:8080/api/mgr/sq_mgr/',headers=head,data=updateData,cookies={"sessionid":sessionid})
    if updateResponse.status_code!=200:
        return updateResponse.status_code
    print('修改课程返回：',updateResponse.json())
    return updateResponse.json()

#----------------------------删除课程1
def delete_course(id,sessionid):
    deleData={
        "action":"delete_course",
        "id":"%s"%id
    }
    head = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    deleResponse=requests.delete('http://localhost:8080/api/mgr/sq_mgr/',headers=head,data=deleData,cookies={"sessionid":sessionid})
    print('删除课程返回：',deleResponse.json())
    return deleResponse.json()

#----------------------------增加课程2
def add2_course(name, desc, display_idx,sessionid):
    courseData = {
        "action": "add_course",
        "data": '''{
          "name":"%s",
          "desc":"%s",
          "display_idx":"%s"
        } ''' % (name, desc, display_idx)
    }
    head = {
        "Content-Type": "application/json"
    }
    addRespsonse = requests.post('http://localhost:8080/apijson/mgr/sq_mgr/', headers=head, json=courseData,cookies={"sessionid":sessionid})
    print('添加课程(json)返回：',addRespsonse.json())
    return addRespsonse.json()


