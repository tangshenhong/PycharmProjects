'''
向sql server数据库批量插入数据时，使用connection.executemany(参数1,参数2)
参数1：sql语句，例如：INSERT INTO sys_area (name,update_time,update_by,classid) VALUES (%s,%s,%s,%d)
参数2：列表，内部元素为元祖。例如：[('zhangsan', '2013-05-20 20:18:16', 'admin',1), ('lisi', '2013-05-20 20:18:16', 'admin',2)]

原文为mysql数据库：https://blog.csdn.net/qq282881515/article/details/70638517
'''

'''
本用例用于进行知识竞赛的数据初始化操作，包括添加院校、团队、人员、考生安排等操作
'''
import pymssql
import time
class ConnectDataBase:
    def __init__(self,server,user,password,database):
        self.server=server
        self.user=user
        self.password=password
        self.database=database
    #连接数据库
    def get_connection(self):
        self.conn=pymssql.connect(self.server,self.user,self.password,self.database)
        self.conn.autocommit(True)
        cursor=self.conn.cursor()
        if not cursor:
            raise (NameError,'连接数据库失败')
        else:
            return cursor
    #插入、删除或者查询数据
    def execute_sql(self,sql,valueList=None,isDele=False):
        cursor=self.get_connection()
        if valueList:#插入数据
            cursor.executemany(sql, valueList)
            self.conn.close()
        elif isDele==True:
            cursor.execute(sql)
        else:#查询数据
            cursor.execute(sql)
            results = cursor.fetchall()
            self.conn.close()
            return results

#----------------------------------------配置信息
# server='192.168.0.108'
server='120.76.247.31'
user='devuser'
password='devuser'
database='ZSJSXT'
#----------------------------------------sql语句
conn_object=ConnectDataBase(server,user,password,database)
#-----------------------------------------数据初始化
conn_object.execute_sql('''DELETE from tbTotalScore where PersonnelID IN (SELECT PersonnelID from tbSigTeamPersonnel where TrueName like '%tsh_%')''',isDele=True)
conn_object.execute_sql('''DELETE FROM tbDTScoreDetail where DTScoreID IN(SELECT tbDTScore.DTScoreID FROM tbDTScore where PersonnelID IN (SELECT tbDTScore.PersonnelID from tbSigTeamPersonnel where TrueName like '%tsh_%'))''',isDele=True)
conn_object.execute_sql('''DELETE FROM tbDTScore where PersonnelID IN (SELECT PersonnelID from tbSigTeamPersonnel where TrueName like '%tsh_%')''',isDele=True)
conn_object.execute_sql('''DELETE FROM tbSJScore WHERE PersonnelID IN (SELECT PersonnelID from tbSigTeamPersonnel where TrueName like '%tsh_%')''',isDele=True)
conn_object.execute_sql('''DELETE FROM tbKCPersonnel WHERE PersonnelID IN(SELECT PersonnelID FROM tbSigTeamPersonnel where IsAccount=1 and TrueName LIKE'%tsh_%')''',isDele=True)
conn_object.execute_sql('''delete from tbSigTeamPersonnel where TrueName like '%tsh_%\'''',isDele=True)
conn_object.execute_sql('''delete FROM tbSigTeam where TeamName LIKE '%tsh团队_%\'''',isDele=True)
conn_object.execute_sql('''delete FROM tbSigSchool where SchoolName LIKE '%tsh院校_%\'''',isDele=True)
#-----------------------------------------
timefield = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
sql_school = '''INSERT INTO tbSigSchool(SchoolNO,SchoolName,PCAID,SchoolAddress,ClassID,Remark,OperationUserID,AddTime,UpdateTime) 
            VALUES(%s,%s,%d,%s,%d,%s,%d,%s,%s)'''
sql_team = '''INSERT INTO tbSigTeam(TeamHeadPicUrl,SchoolID,TeamName,TeamSlogan,TeamDescribe,Remark,OperationUserID,AddTime,UpdateTime) 
            VALUES(%s,%d,%s,%s,%s,%s,%d,%s,%s)'''
sql_personnel='''INSERT INTO tbSigTeamPersonnel(TeamID,SchoolID,PersonnelNO,Password,TrueName,TeamRole,Phone,Email,IdCard,Professional,HeadPicUrl,OrderNO,Remark,OperationUserID,AddTime,UpdateTime,IsAccount,TextPasswords) 
            VALUES(%d,%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%s,%d,%s,%s,%d,%s)'''
#考生安排表
sql_KCPersonnel='''INSERT INTO tbKCPersonnel(KCID,PersonnelID,KSDate,IsJoin,Remark,OperationUserID,AddTime,UpdateTime) VALUES(%d,%d,%s,%d,%s,%d,%s,%s)'''
schoolValues=[]
teamValues=[]
personnelValues=[]
KCPersonnelValues=[]
#----------------------------------------插入院校
for i in range(1, 242):
    schoolValues.append((f'院校编码{i}', f'tsh院校_{i}', 151, f'院校地址{i}', 52, f'备注{i}', 2, timefield, timefield))
conn_object.execute_sql(sql_school,schoolValues)
#----------------------------------------插入团队
    #获取所有院校
schoolid_list=conn_object.execute_sql("SELECT SchoolID FROM tbSigSchool where SchoolName LIKE '%tsh院校_%' order by SchoolID")
for idx,schoolid in enumerate(schoolid_list):
    teamValues.append(('/Content/img/noImg.png',schoolid, f'tsh团队_{idx+1}', f'团队口号{idx+1}：加油加油加油你是最棒的', f'团队描述{idx+1}：这是来自XX院校的XX团队，这是一支强劲的队伍', f'团队备注{idx+1}', 2, timefield, timefield))
conn_object.execute_sql(sql_team,teamValues)
#----------------------------------------插入人员
    #获取所有团队
team_list=conn_object.execute_sql("SELECT SchoolID,TeamID FROM tbSigTeam where TeamName LIKE '%tsh团队_%' order by TeamID")
for idx,team in enumerate(team_list):
    personnelValues.append((team[1], team[0], f'考生编号{idx + 1}', 'E10ADC3949BA59ABBE56E057F20F883E', f'tsh_{idx + 1}', 0,
                            '15741253650', '123@123.com', '3504261990', f'专业{idx + 1}', '/Content/img/noImg.png', 0,
                            f'备注{idx + 1}', 2, timefield, timefield, 1, '123456'))
conn_object.execute_sql(sql_personnel,personnelValues)
#----------------------------------------插入考生安排，安排到考场“tsh考场”
    #获取所有考生账号
person_list=conn_object.execute_sql("SELECT PersonnelID FROM tbSigTeamPersonnel where IsAccount=1 and TrueName LIKE'%tsh_%' AND PersonnelID NOT IN(SELECT PersonnelID from tbKCPersonnel)")
for person in person_list:
    KCPersonnelValues.append((36,person[0],'2019-10-22 12:00:00.000',0,None,2,'2019-10-22 17:09:38.353',None))
    # KCPersonnelValues.append((1, person[0], '2019-10-22 12:00:00.000', 0, None, 2, '2019-10-22 17:09:38.353', None))
conn_object.execute_sql(sql_KCPersonnel,KCPersonnelValues)


