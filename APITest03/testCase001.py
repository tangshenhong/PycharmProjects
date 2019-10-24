from APITest03.APIClass import *
#创建教师管理实例
tm=TeacherMgr()
#登录
loginResponse=tm.login('auto','sdfsdfsdf')
assert loginResponse['retcode']==0
# 创建课程管理实例
cm = CourseMgr(tm.sessionid)
#添加一门课程
addCourseResp=cm.add_course('math1','math1的desc',1)
assert addCourseResp['retcode']==0
course=[{"id":addCourseResp['id'],"name":"math1"}]
#添加一位教师
addTeacherResp1=tm.add_teacher('teacher1','111111','tsh','tsh的desc',course,1)
assert addTeacherResp1['retcode']==0
#列出教师列表before
beforeTeachers=tm.list_teacher()['retlist']
#再添加一位同名教师
addTeacherResp2=tm.add_teacher('teacher1','111111','tsh','tsh的desc',course,1)
assert addTeacherResp2['retcode']==1
#列出教师列表after
afterTeachers=tm.list_teacher()['retlist']
#比较before和after是否相等
assert beforeTeachers==afterTeachers

#删除课程
cm.delete_course(addCourseResp['id'])
#删除教师
tm.delete_teacher(addTeacherResp1['id'])
print('----case pass----')