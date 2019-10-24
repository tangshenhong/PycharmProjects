from APITest.APIClass import  *
#先登录
loginResponse,cookies=login('auto','sdfsdfsdf')
assert loginResponse['retcode']==0
sessionid=cookies['sessionid']

# 添加一门课程
addResponse1=add_course('test','test','1',sessionid)
assert addResponse1['retcode']==0

# 先列出课程
beforeCourses=list_course(sessionid)['retlist']

#再添加一门课程
addResponse2=add_course('test','test','1',sessionid)
assert addResponse2['retcode']==2

# 再列出课程
afterCourses=list_course(sessionid)['retlist']

#比较两次课程有无变化
assert beforeCourses==afterCourses

# 清除环境操作
delete_course(addResponse1['id'],sessionid)
print('----case pass----')
