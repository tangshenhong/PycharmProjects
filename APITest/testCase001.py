from APITest.APIClass import *
#先登录
loginResponse,cookies=login('auto','sdfsdfsdf')
assert loginResponse['retcode']==0
sessionid=cookies['sessionid']

# 先列出课程
beforeCourses=list_course(sessionid)['retlist']

# 添加一门课程
addResponse=add_course('courseTest', 'courseTest', '1',sessionid)
assert addResponse['retcode']==0

# 再列出课程
afterCourses=list_course(sessionid)['retlist']
#将多出来的一门课程取出
newCourse={}
for one in afterCourses:
    if one not in beforeCourses:
        newCourse=one
        break
# 检查是否是刚刚添加的课程
assert newCourse['name']=='courseTest'
assert newCourse['desc']=='courseTest'
assert newCourse['display_idx']==1

# 清除环境操作
delete_course(addResponse['id'],sessionid)
print('----case pass----')
