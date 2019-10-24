from APITest03.APIClass import *
from random import randint
#登录
tm=TeacherMgr()
tm.login('auto','sdfsdfsdf')
cm=CourseMgr(tm.sessionid)
#添加一门课程
addCourseResp=cm.add_course('course1','course1的desc',1)
assert addCourseResp['retcode']==0
courseId=addCourseResp['id']
course=[{"id":addCourseResp['id'],"name":"course1"}]
#添加一名教师，起名用随机数
name=f'teacher_{randint(1,99999)}'
addTeacherResp=tm.add_teacher(name,'111111','ttt','ttt的desc',course,1)
assert addTeacherResp['retcode']==0
teacherId=addTeacherResp['id']
#列出教师
tm.list_teacher()['retlist']
#修改这名教师的姓名
newName=f'teacher_{randint(1,99999)}'
modifyTeacherResp=tm.modify_teacher(teacherId, newName, '111111', 'ttt', 'ttt的desc', course, 1)
assert modifyTeacherResp['retcode']==0
#列出教师
teacherList=tm.list_teacher()['retlist']
#检查姓名是否成功修改
modifyTeacher=[teacher for teacher in teacherList if teacher['id'] == teacherId]
assert modifyTeacher[0]['username']==newName

#删除课程
cm.delete_course(courseId)
#删除教师
tm.delete_teacher(teacherId)
print('----case pass----')