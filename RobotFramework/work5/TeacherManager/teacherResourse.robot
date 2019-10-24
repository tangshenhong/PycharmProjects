*** Settings ***
Resource   ../Tools/initialize.robot
Resource  ../CoursesManage/courseResourse.robot
Library  SeleniumLibrary
Library  Collections
*** Keywords ***
setupTeacher
    deleteTeachers
    deleteCourses
     #添加课程
    addCourse  初中语文     初中语文的描述     1
    addCourse  初中数学     初中数学的描述     2
    ${exceptCourses}     create list  初中语文   初中数学
    courseVerification  ${exceptCourses}

teardownTeacher
    deleteTeachers
    deleteCourses
deleteTeachers
    click element  css:[href="#/teacher"]
    sleep  1
    set browser implicit wait  2
    FOR  ${one}  IN RANGE  1000
        ${deleElements}    SeleniumLibrary.Get WebElements  css:[ng-click="delOne(one)"]
        exit for loop if  $deleElements==[]
        click element  ${deleElements[0]}
        click element  css:.btn.btn-primary
        sleep  1
    END
    set browser implicit wait  10

addTeacher
    click element  css:[href="#/teacher"]
    sleep  1
    [Arguments]  ${realname}    ${username}   ${desc}   ${display_idx}  ${coursename}
    click element  css:[ng-click="showAddOne=true"]
    input text  css:[ng-model="addEditData.realname"]   ${realname}
    input text  css:[ng-model="addEditData.username"]   ${username}
    input text  css:[ng-model="addEditData.desc"]    ${desc}
    input text  css:[ng-model="addEditData.display_idx"]    ${display_idx}
    select from list by label   css:[ng-model="$parent.courseSelected"]   ${coursename}
    click element  css:[ng-click="addOne()"]
    sleep  1
teacherVerification
    [Arguments]  ${expects}
    ${realElements}  SeleniumLibrary.Get WebElements  css:tbody>tr>td:nth-child(2) span
    ${reals}    create list
    FOR  ${one}  IN  @{realElements}
        append to list  ${reals}    ${one.text}
    END
    should be equal  ${expects}     ${reals}
