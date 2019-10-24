from APITest.APIClass import *
loginRes,cookies=login('auto','sdfsdfsdf')
assert loginRes['retcode']==0
sessionid=cookies['sessionid']
#先添加一门课程
addResp=add_course('测试删除课程','测试删除课程的描述','1',sessionid)
assert addResp['retcode']==0
deleId=addResp['id']

#列出删除前课程
beforeCourses=list_course(sessionid)['retlist']

#删除课程
deleResp=delete_course(deleId,sessionid)
assert deleResp['retcode']==0

#列出删除后课程
afterCourses=list_course(sessionid)['retlist']

#查看被删除课程id是否在afterCourses里
for one in afterCourses:
    assert one['id']!=deleId

print('----case pass----')
