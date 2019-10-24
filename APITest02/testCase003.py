from datetime import datetime
from APITest02.APIClass import cm

#先登录
loginResponse=cm.login('auto','sdfsdfsdf')
assert loginResponse['retcode']==0
#添加课程1
addResp1=cm.add_course('course111','course111的描述',1)
assert addResp1['retcode']==0
id1=addResp1['id']

#添加课程2
addResp2=cm.add_course('course222','course222的描述',2)
assert addResp2['retcode']==0
id2=addResp2['id']

#列出修改前课程
beforeCourses=cm.list_course()['retlist']

#----------------情况一：对课程1的课程名进行修改，确保新课程名与系统已有课程名不重复
firstUpdate=f'course111{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
updateResp=cm.update_course(id1,firstUpdate,'course111的描述',1)
assert  updateResp['retcode']==0

#列出修改后课程
afterCourses=cm.list_course()['retlist']
assert len(beforeCourses)==len(afterCourses)
#确认修改后的新课程名在原列表里不存在
for one in beforeCourses:
    assert one['name'] != firstUpdate
#确认课程已正确修改
for one in afterCourses:
    if one['id']==id1:
        assert one['name']==firstUpdate
        assert one['desc']=='course111的描述'
        assert one['display_idx']==1
        break

# ----------------情况二：将课程名1修改为课程名2，应不可提交。但服务器未针对这种情况返回值，因此检查状态码是否!=200
updateResp2=cm.update_course(id1,'course222','course111的描述',1)
assert  updateResp2!=200
#列出课程
afterCourses2=cm.list_course()['retlist']
#确认课程名1未修改成功
assert afterCourses==afterCourses2

#删除添加的两个课程
cm.delete_course(id1)
cm.delete_course(id2)

print('----case pass----')