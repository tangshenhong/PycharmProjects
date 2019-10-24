#-*- coding:utf-8 -*-
'''
本用例用于招标代理业务测试  接口测试
'''
from ZJZX.ToolClass.LoginClass import *
url = 'http://120.76.247.31:1607'
#登录操作
login=LoginClass()
status,session=login.login(url,'admin','123456')
assert  status==200
#点击“招标代理业务”菜单
pmresp=session.get(url+'/Proxy/Proxy/ProxyIndex')
assert pmresp.status_code==200
#___________________________________________________________________________收件登记任务开始
#点击添加按钮
proxyaddresp=session.get(url+'/Proxy/Proxy/PrProInfoAddOrEdit?IsHaveTCK=True')
assert proxyaddresp.status_code==200
#上传附件
#——————————上传带有中文的文件名，报错，解决方法参考：https://blog.csdn.net/jylonger/article/details/82386868
#——————————python处理multipart/form-data的请求方法，参考：https://www.jb51.net/article/153516.htm
files={"Filename":(None,"word文档测试.docx"),"Filedata":("word文档测试.docx",open("G:\常用测试素材\word文档测试.docx","rb")),"Upload":(None,"Submit Query")}
fileresp=session.post(url +"/Systems/FileUpload/FileUpload",files=files)
print('上传附件返回：',fileresp.text)
assert  fileresp.status_code==200
#获取附件上传后的存放地址
annexname=fileresp.json()['AppendData']['filename']
fullname=fileresp.json()['AppendData']['fullname']
#收件登记保存操作
savedata={
"ProInfoID": 0,
"IsWorkFlow": False,
"TasksID":"" ,
"ProNo": "0515",
"ProName": "pythontest",
"ProType": "公开招标",
"IsFile": True,
"IsFile": False,
"UnitName": "晨曦",
"ContactInformation": "15705944206",
"TradingPlace": "福州",
"ProScale":"很大" ,
"BuildingDate": "2019-05-15",
"Remark": "基础信息备注",
"AnnexJsonString":'''[{"AnnexName":"%s","AnnexAddress":"%s","AnnexClassID":"103","Remark":"附件备注"}]'''%(annexname,fullname),
"AnnexClassID": "103",
"AnnexName": {annexname},
"AnnexAddress": {fullname},
"Remark": "基础信息备注",
"AnnexClassID": "103",
"AnnexName": "",
"AnnexAddress":"" ,
"Remark": "",
"X-Requested-With": "XMLHttpRequest"
}
saveheads={
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
}
saveresp=session.post("http://120.76.247.31:1607/Proxy/Proxy/PrProInfoAddOrEdit",data=savedata,headers=saveheads)
print('收件登记保存返回：',saveresp.text)
assert saveresp.status_code==200
#收件登记提交操作
#收件登记审核操作