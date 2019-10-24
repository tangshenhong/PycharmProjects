#本用例用于确认菜单请求是否均返回200状态码
from pymssql import *
import time
from ZJZX.ToolClass.LoginClass import *


class CheckMenuUrl:
    count=0
    def __init__(self,server,user,password,database):

        self.server=server
        self.user=user
        self.password=password
        self.database=database

    def get_connection(self):
        self.conn=connect(self.server,self.user,self.password,self.database)
        self.conn.autocommit(True)
        cursor=self.conn.cursor()
        if not cursor:
            raise (NameError,'连接数据库失败')
        else:
            return cursor
    def execute_sql(self,sql):
        cursor=self.get_connection()
        cursor.execute(sql)
        results=cursor.fetchall()
        self.conn.close()
        return results

#----------------------------------------配置信息
#大禹测试
url = 'http://192.168.0.108:1606/'
server='192.168.0.108'
user='devuser'
password='devuser'
database='ZJZX_DY_C'

sql='select MenuURL,MenuName,MenuID,ParentMenuID from tbSysMenu where MenuURL IS NOT NULL AND MenuLevel=0 AND Visible=1'
#----------------------------------------
#登录操作
login=LoginClass()
status,session=login.login(url,'admin','123456')
assert  status==200
#连接数据库，并执行语句，获得结果集
checkObject=CheckMenuUrl(server,user,password,database)
results=checkObject.execute_sql(sql)
#遍历结果集，拼接出菜单get请求语句
checkResult='OK'
for result in results:
    responseStatusCode=session.get(url+result[0]).status_code
    if responseStatusCode!=200:
        print('--------------------------------------------------------------------------------------------------------------------------')
        print(f'\t名称：{result[1]:<10}\tid：{result[2]:<10}\t菜单地址：{result[0]:<40}\t父节点id：{result[3]:<10}')
        # print(f'状态码：{responseStatusCode}\n内容：{session.get(url+result[0]).text }',)
        checkResult='不OK'
if checkResult=='OK':
    print('\n--testcase pass 没有菜单报错--')
else:
    print('\n--testcase not pass 报错信息如上--')