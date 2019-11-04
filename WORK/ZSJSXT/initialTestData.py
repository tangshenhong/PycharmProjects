# -*- coding: utf-8 -*-
'''
向sql server数据库批量插入数据时，使用connection.executemany(参数1,参数2)
参数1：sql语句，例如：INSERT INTO sys_area (name,update_time,update_by,classid) VALUES (%s,%s,%s,%d)
参数2：列表，内部元素为元祖。例如：[('zhangsan', '2013-05-20 20:18:16', 'admin',1), ('lisi', '2013-05-20 20:18:16', 'admin',2)]
原文为mysql数据库：https://blog.csdn.net/qq282881515/article/details/70638517
'''

'''
本用例用于进行知识竞赛的数据初始化操作，包括添加院校、团队、人员、考生安排等操作
'''


import time
from WORK.tools.DataBaseOperation import DataBaseOperation

class InitializeTestData():
    '''用于初始化数据、插入数据等操作'''
    def __init__(self,server,user='devuser',password='devuser',database='ZSJSXT'):
        self._server = server
        self._user = user
        self._password = password
        self._database = database
        #获取数据库连接
        self.conn_object=DataBaseOperation(server, user, password, database)
        # 唯一时间标识
        self.timeLabel = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def setUp(self):
        '''
        初始化数据（删除），删除语句在config/delete.sql中
        '''
        with open('config/delete.sql','r') as f:
            sqls=f.readlines()
        for sql in sqls:
            self.conn_object.execute_sql(
                f'''{sql}''',
                isDele=True)

    def insertSchool(self,num=0):
        '''
        插入院校
        :param num:插入的数据条数
        '''
        sql_school = '''INSERT INTO tbSigSchool(SchoolNO,SchoolName,PCAID,SchoolAddress,ClassID,Remark,OperationUserID,AddTime,UpdateTime)
                    VALUES(%s,%s,%d,%s,%d,%s,%d,%s,%s)'''
        schoolValues = []
        for i in range(1, num+1):
            schoolValues.append((f'院校编码{i}', f'tsh院校_{i}', 151, f'院校地址{i}', 52, f'备注{i}', 2, self.timeLabel, self.timeLabel))
        self.conn_object.execute_sql(sql_school, schoolValues)

    def insertTeam(self):
        '''
        插入团队
        '''
        sql_team = '''INSERT INTO tbSigTeam(TeamHeadPicUrl,SchoolID,TeamName,TeamSlogan,TeamDescribe,Remark,OperationUserID,AddTime,UpdateTime)
                    VALUES(%s,%d,%s,%s,%s,%s,%d,%s,%s)'''
        teamValues=[]
        # 获取所有院校
        schoolid_list = self.conn_object.execute_sql(
            "SELECT SchoolID FROM tbSigSchool where SchoolName LIKE '%tsh院校_%' order by SchoolID")
        for idx, schoolid in enumerate(schoolid_list):
            teamValues.append(('/Content/img/noImg.png', schoolid, f'tsh团队_{idx + 1}', f'团队口号{idx + 1}：加油加油加油你是最棒的',
                               f'团队描述{idx + 1}：这是来自XX院校的XX团队，这是一支强劲的队伍', f'团队备注{idx + 1}', 2, self.timeLabel, self.timeLabel))
        self.conn_object.execute_sql(sql_team, teamValues)

    def insertPerson(self):
        '''
        插入人员
        '''
        sql_personnel = '''INSERT INTO tbSigTeamPersonnel(TeamID,SchoolID,PersonnelNO,Password,TrueName,TeamRole,Phone,Email,IdCard,Professional,HeadPicUrl,OrderNO,Remark,OperationUserID,AddTime,UpdateTime,IsAccount,TextPasswords)
                    VALUES(%d,%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%s,%d,%s,%s,%d,%s)'''
        personnelValues=[]
        # 获取所有团队
        team_list = self.conn_object.execute_sql(
            "SELECT SchoolID,TeamID FROM tbSigTeam where TeamName LIKE '%tsh团队_%' order by TeamID")
        for idx, team in enumerate(team_list):
            personnelValues.append(
                (team[1], team[0], f'考生编号{idx + 1}', 'E10ADC3949BA59ABBE56E057F20F883E', f'tsh_{idx + 1}', 0,
                 '15741253650', '123@123.com', '3504261990', f'专业{idx + 1}', '/Content/img/noImg.png', 0,
                 f'备注{idx + 1}', 2, self.timeLabel, self.timeLabel, 1, '123456'))
        self.conn_object.execute_sql(sql_personnel, personnelValues)

    def insertKC(self):
        '''
        插入tsh考场
        :return: 返回插入的考场ID
        '''
        #确认考卷是否存在
        kjID=self.conn_object.execute_sql("SELECT KJID from tbKJ where KJTitle='tsh考卷'")
        if not kjID:
            raise Exception('不存在tsh考卷，请手动新建考卷！！')
        #插入考场
        sql_KC = '''INSERT INTO tbKC(KCTitle,Subtitle,KJID,KCImgID,BeginDate,EndTDate,LimitModifyTime,IsUse,Remark,OperationUserID,AddTime,UpdateTime) 
            VALUES(%s,%s,%d,%d,%s,%s,%d,%d,%s,%d,%s,%s)'''
        kcValue = [('tsh考场', None,kjID[0][0], None, '2019-11-04 12:00:00.000', '2020-01-01 12:00:00.000', 3, 1, None, 2,
                    '2019-11-04 12:00:00.000', '2019-11-04 12:00:00.000')]
        self.conn_object.execute_sql(sql_KC, kcValue)
        kcID=self.conn_object.execute_sql("SELECT KCID from tbKC where KCTitle='tsh考场'")[0][0]
        return kcID

    def kCPersonnel(self):
        '''
        考生考场安排
        '''
        #插入考场，获取考场ID
        kcID=self.insertKC()
        #进行考场安排
        sql_KCPersonnel = '''INSERT INTO tbKCPersonnel(KCID,PersonnelID,KSDate,IsJoin,Remark,OperationUserID,AddTime,UpdateTime) VALUES(%d,%d,%s,%d,%s,%d,%s,%s)'''
        KCPersonnelValues=[]
        # 获取所有tsh_考生账号
        person_list = self.conn_object.execute_sql(
            "SELECT PersonnelID FROM tbSigTeamPersonnel where IsAccount=1 and TrueName LIKE'%tsh_%' AND PersonnelID NOT IN(SELECT PersonnelID from tbKCPersonnel)")
        for person in person_list:
            KCPersonnelValues.append(
                (kcID, person[0], '2019-10-22 12:00:00.000', 0, None, 2, '2019-10-22 17:09:38.353', None))
            # KCPersonnelValues.append((1, person[0], '2019-10-22 12:00:00.000', 0, None, 2, '2019-10-22 17:09:38.353', None))
        self.conn_object.execute_sql(sql_KCPersonnel, KCPersonnelValues)


if __name__ == '__main__':
    # 数据库服务器ip
    # server='192.168.0.108'
    server = '120.76.247.31'
    try:
        init = InitializeTestData(server)
        init.setUp()
        init.insertSchool(240)
        init.insertTeam()
        init.insertPerson()
        init.kCPersonnel()
    except  Exception:
        raise
    else:
        print('测试数据新建成功~')