# -*- coding: utf-8 -*-
'''
将Excel数据插入到数据库中
'''
from WORK.tools.DataBaseOperation import DataBaseOperation
from openpyxl import load_workbook

def getExcelValues():
    #读取excel
    wb=load_workbook('import.xlsx')
    #读取第一个默认sheet
    sheet=wb.active
    return sheet.values

sql='''INSERT INTO tbSigTeamPersonnel(TeamID,SchoolID,PersonnelNO,Password,TrueName,TeamRole,Phone,Email,IdCard,Professional,HeadPicUrl,OrderNO,Remark,OperationUserID,AddTime,UpdateTime,IsAccount,TextPasswords) 
VALUES(%d,%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%s,%d,%s,%s,%d,%s)'''
database=DataBaseOperation(database='ZSJSXT')
insertValues=[]
excelValues=getExcelValues()
for idx,row in enumerate(excelValues):
    if idx==0:
        continue
    insertValues.append((None,None,row[0],'E10ADC3949BA59ABBE56E057F20F883E',row[1],0,row[2],None,None,None,None,0,None,2,'2019-11-08 16:14:02.007',None,0,None))
database.execute_sql(sql,insertValues)
