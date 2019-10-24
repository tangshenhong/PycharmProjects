*** Settings ***
Resource   ../Tools/initialize.robot
Resource  teacherResourse.robot
Suite Setup  setupBrower
Suite Teardown  closeProcess
*** Test Cases ***
addTeacher
    [Setup]  setupTeacher
    #添加教师
    addTeacher  realname2   loginname2  desc2   2   初中语文
    addTeacher  realname1   loginname1  desc1   1   初中数学
    ${exceptTeachers}   create list  realname1  realname2
    teacherVerification     ${exceptTeachers}
    [Teardown]  teardownTeacher