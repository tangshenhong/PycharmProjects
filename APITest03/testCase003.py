from APITest03.APIClass import *
#创建教师实例
tm=TeacherMgr()
#登录
loginResp=tm.login('auto','sdfsdfsdf')
assert loginResp['retcode']==0
#创建课程实例
cm=CourseMgr(tm.sessionid)
#列出教师before
beforeTeachers=tm.list_teacher()['retlist']
#添加课程
addCourseResp=cm.add_course('course1','course1的desc',1)
assert addCourseResp['retcode']==0
courseId=addCourseResp['id']
course=[{"id":courseId,"name":"course1"}]
#添加教师
addTeacherResp=tm.add_teacher('teacher1','111111','ttt','teacher1的desc',course,1)
assert addTeacherResp['retcode']==0
teacherId=addTeacherResp['id']
#删除教师
deleteTeacherResp=tm.delete_teacher(teacherId)
assert deleteTeacherResp['retcode']==0
#列出教师after
afterTeachers=tm.list_teacher()['retlist']
#比较before和after是否相等
assert beforeTeachers==afterTeachers

#----清除环境操作：删除课程
cm.delete_course(courseId)
print('----case pass----')