# -*- coding: utf-8 -*-
'''
将数据库数据读取到Excel中
'''
from openpyxl import Workbook
from WORK.tools.DataBaseOperation import DataBaseOperation
def writeToExcel(exportPersons):
    #新建excel
    wb=Workbook()
    #获得默认第一个sheet
    sheet=wb.active
    #设置sheet标题
    sheet.title='导出内容'
    #以列表形式，插入一行
    sheet.append(['团队名称','院校名称','考生编号','考生姓名','团队角色'])
    for person in exportPersons:
        sheet.append(person)
    wb.save('export.xlsx')

sql='''SELECT tt.TeamName,ts.SchoolName,PersonnelNO,TrueName,tp.TeamRole from tbSigTeamPersonnel tp,tbSigSchool ts,tbSigTeam tt WHERE tp.SchoolID=ts.SchoolID AND tp.TeamID=tt.TeamID'''
database=DataBaseOperation(database='ZSJSXT')
exportPersons=[]
dbDatas=database.execute_sql(sql)
for person in dbDatas:
    print(person[0],person[1],person[2],person[3],person[4])
    exportPersons.append([person[0],person[1],person[2],person[3],person[4]])
writeToExcel(exportPersons)
