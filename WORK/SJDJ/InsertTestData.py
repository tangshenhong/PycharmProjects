'''
向sql server数据库批量插入数据时，使用connection.executemany(参数1,参数2)
参数1：sql语句，例如：INSERT INTO sys_area (name,update_time,update_by,classid) VALUES (%s,%s,%s,%d)
参数2：列表，内部元素为元祖。例如：[('zhangsan', '2013-05-20 20:18:16', 'admin',1), ('lisi', '2013-05-20 20:18:16', 'admin',2)]

原文为mysql数据库：https://blog.csdn.net/qq282881515/article/details/70638517
'''

# -----------------------------------------------本用例用于向自来水的收件登记4个模块批量插入数据
import pymssql
import time
from random import randint
class ConnectDataBase:
    def __init__(self,server,user,password,database):
        self.server=server
        self.user=user
        self.password=password
        self.database=database
    def get_connection(self):
        self.conn=pymssql.connect(self.server,self.user,self.password,self.database)
        self.conn.autocommit(True)
        cursor=self.conn.cursor()
        if not cursor:
            raise (NameError,'连接数据库失败')
        else:
            return cursor
    def execute_sql(self,sql,valueList=None):
        cursor=self.get_connection()
        if valueList:#插入数据
            cursor.executemany(sql, valueList)
            self.conn.close()
        else:#查询数据
            cursor.execute(sql)
            results = cursor.fetchall()
            self.conn.close()
            return results
#----------------------------------------配置信息
server='192.168.0.108'
user='devuser'
password='devuser'
database='SJDJSYS'
#----------------------------------------
conn_object=ConnectDataBase(server,user,password,database)
sql='''INSERT INTO tbProInfo(ClassID,PlanNO,ProNO,ProName,CheckMoney,ConstructionTeam,SendUnitNO,SendUnit,SendUser,SendCheckTime,Remark,CollectionUser,IsCheck,RepairNO,State,OperationUserID,AddTime,UpdateTime,OrdersType,IsSpotCheck,SendUserPhone,SerialNumber,CostClassID,CompletionTime,AcceptanceTime,Code,IsArchive,IsSeal,CheckDistributionTime,CheckFinishTime,ArchiveTime,SealTime,ParentProInfoID) 
VALUES(%d,%s,%s,%s,%d,%s,%s,%s,%s,%s,%s,%d,%d,%s,%d,%d,%s,%s,%d,%d,%s,%s,%d,%s,%s,%s,%d,%d,%s,%s,%s,%s,%s)'''
# #直接内审项目类别
# classid_list=conn_object.execute_sql('SELECT * from tbProClass where IsUse=1 AND ParentClassID=4 AND ClassName LIKE \'%庭院管网1%\' OR ClassName LIKE \'%户表1%\' OR ClassName LIKE \'%管道抢修%\' OR ClassName LIKE \'泵房\' OR ClassName LIKE \'%破路费%\'')
#获取所有项目类别
classid_list=conn_object.execute_sql('SELECT * from tbProClass where IsUse=1 AND ParentClassID=4')
#获取费用类别
costclassid_list=conn_object.execute_sql('SELECT ClassID from tbProClass where IsUse=1 AND ParentClassID=14')
#添加4个收件登记模块的测试数据
valuelist=[]
for type in range(1):#0普通件，1 重大件，2 量价件,3财审件
    for i in range(1, 1001):
        timee = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 随机抽取项目类别id
        classnum = randint(0, len(classid_list) - 1)
        classid = classid_list[classnum][0]
        # 随机抽取费用类别id
        costnum = randint(0, len(costclassid_list) - 1)
        costid = costclassid_list[costnum][0]
        if type==0:
            proname='普通登记'
        elif type==1:
            proname = '重大基建'
        elif type==2:
            proname='量价件'
        else:
            proname='财审件'
        valuelist.append((
            classid, f'计划编号{i}', f'工程编号{i}', f'{proname}{i}', i, f'施工单位{i}', f'送审单位编号{i}', f'送审单位{i}', f'送件人员{i}', timee,
            f'备注{i}', 2, 0, f'维修编号{i}', 0, 2, timee, timee, type, 0, f'15704152632电话{i}', f'2019-00{i}', costid,
            timee, timee, f'编码{i}', 0, 0,timee,timee,timee,timee,None))
conn_object.execute_sql(sql, valuelist)


