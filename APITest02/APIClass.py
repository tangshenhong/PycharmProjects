import requests
from pprint import pprint
class APIBase:
    #登录操作
    def login(self,username,password):
        head={
            "Host":"localhost:8080",
            "Content-Type":"application/x-www-form-urlencoded"
        }
        payload={
            "username":username,
            "password": password
        }
        resp=requests.post('http://localhost:8080/api/mgr/loginReq', headers=head, data=payload)
        self.sessionid=resp.cookies['sessionid']
        print('登录返回：',resp.json())
        return resp.json()
#-----------------------------------------------course管理类
class CourseMgr(APIBase):
    #添加一门课程（系统中不存在、系统中已存在）
    def add_course(self,name,desc,display_idx):
        payload={
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
        resp=requests.post('http://localhost:8080/api/mgr/sq_mgr/',headers=head, data=payload,cookies={"sessionid":self.sessionid})
        print('添加课程返回：',resp.json())
        return resp.json()
    #列出课程
    def list_course(self):
        resp=requests.get('http://localhost:8080/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20',cookies={"sessionid":self.sessionid})
        print('列出课程返回：')
        pprint(resp.json())
        return resp.json()

    #修改课程
    def update_course(self,id,name,desc,display_idx):
        payload={
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
        resp=requests.put('http://localhost:8080/api/mgr/sq_mgr/',headers=head,data=payload,cookies={"sessionid":self.sessionid})
        if resp.status_code!=200:
            return resp.status_code
        print('修改课程返回：',resp.json())
        return resp.json()

    #-删除课程1
    def delete_course(self,id):
        payload={
            "action":"delete_course",
            "id":"%s"%id
        }
        head = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        resp=requests.delete('http://localhost:8080/api/mgr/sq_mgr/',headers=head,data=payload,cookies={"sessionid":self.sessionid})
        print('删除课程返回：',resp.json())
        return resp.json()

    #增加课程2（json格式）
    def add2_course(self,name, desc, display_idx):
        payload = {
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
        resp = requests.post('http://localhost:8080/apijson/mgr/sq_mgr/', headers=head, json=payload,cookies={"sessionid":self.sessionid})
        print('添加课程(json)返回：',resp.json())
        return resp.json()

#创建课程管理实例
cm=CourseMgr()

#-----------------------------------------------teacher管理类
import json
class TeacherMgr(APIBase):
    def add_teacher(self,username,password,realname,desc,courses,display_idx):
        payload={
            "action":"add_teacher",
            "data":f'''{{
            "username": "{username}",
            "password": "{password}",
            "realname": "{realname}",
            "desc": "{desc}",
            "courses": {json.dumps(courses)},
            "display_idx":display_idx
            }}'''
        }
        head={
            "Content - Type": "application / x - www - form - urlencoded"
        }
        resp=requests.post('http://localhost:8080/api/mgr/sq_mgr/',data=payload)
        return resp.json()

    def list_teacher(self,pagenum=1,pagesize=20):
        params={
            "action":"list_teacher",
            "pagenum":pagenum,
            "pagesize":pagesize
        }
        head={
            "Content - Type": "application / x - www - form - urlencoded"
        }
        resp=requests.get('http://localhost:8080/api/mgr/sq_mgr/',params=params,head=head)
        return resp.json()
    def modify_teacher(self,username,password,realname,desc,courses,display_idx):
        payload={
            "action":"modify_teacher",
            "data":f'''{{
                "username":"{username}",
                "password":"{password}",
                "realname":"{realname}",
                "desc":"{desc}",
                "courses":{json.dumps(courses)},
                "display_idx":{display_idx}
            }}'''
        }
        head={
            "Content - Type": "application / x - www - form - urlencoded"
        }
        resp=requests.put('http://localhost:8080/api/mgr/sq_mgr/',data=payload,head=head)
        return resp.json()
    def delete_teacher(self,id):
        payload={
            "action":"delete_teacher",
            "id":id
        }
        head={
            "Content - Type": "application / x - www - form - urlencoded"
        }
        resp=requests.delete('http://localhost:8080/api/mgr/sq_mgr/',data=payload,head=head)
        return resp.json()