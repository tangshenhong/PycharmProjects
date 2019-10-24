from APITest02.APIClass import cm

loginRes=cm.login('auto','sdfsdfsdf')
assert loginRes['retcode']==0

#列出原始课程
beforeCourses=cm.list_course()['retlist']

#先添加一门课程
addResp=cm.add_course('测试删除课程','测试删除课程的描述','1')
assert addResp['retcode']==0
deleId=addResp['id']

#删除课程
deleResp=cm.delete_course(deleId)
assert deleResp['retcode']==0

#列出删除后课程
afterCourses=cm.list_course()['retlist']

#查看删除前后的课程列表是否相同
assert beforeCourses==afterCourses

print('----case pass----')
