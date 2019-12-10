*** Settings ***
Library  pylib.ClassManageResource

*** Test Cases ***
添加班级2_tc000002
    #添加班级
    ${dict1}    add_class   1   班级2     102
    should be true  $dict1['retcode']==0
    #验证是否添加成功
    ${dict2}    list_classes_by_schoolgrade     1
    ${classes}      evaluate  $dict2['retlist']
    FOR     ${class}    IN      @{classes}
        continue for loop if    $class['id']!=$dict1['id']
        should be true      $class['name']=='班级2'
        should be true      $class['grade__name']=='七年级'
        should be true      $class['invitecode']==$dict1['invitecode']
        should be true      $class['studentlimit']==102
        should be true      $class['studentnumber']==0
        should be true      $class['teacherlist']==[]
        exit for loop
    END
    [Teardown]  delete_class_by_classid     &{dict1}[id]
