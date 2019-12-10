*** Settings ***
Library  pylib.ClassManageResource

*** Test Cases ***
添加班级1_tc000001
    #添加班级
    ${dict1}   add_class   1   班级1     101
    should be true      $dict1['retcode']==0
    #验证是否添加成功
    ${dict2}     list_classes_by_schoolgrade     1
    ${class}     evaluate  $dict2['retlist'][0]
    should be true      $class['name']=='班级1'
    should be true      $class['grade__name']=='七年级'
    should be true      $class['invitecode']==$dict1['invitecode']
    should be true      $class['studentlimit']==101
    should be true      $class['studentnumber']==0
    should be true      $class['id']==$dict1['id']
    should be true      $class['teacherlist']==[]
    [Teardown]  delete_class_by_classid     &{dict1}[id]

