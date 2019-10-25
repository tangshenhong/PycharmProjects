*** Settings ***
Library  SeleniumLibrary
Library  pylib.Resource.WebOpAdmin
*** Test Cases ***
addCourse
    [Setup]  DeleteAllCourse
    AddCourse   课程2  课程2的描述  2
    sleep  2
    ${expectCourses1}  create list  课程2
    checkCourse  ${expectCourses1}
    AddCourse   课程1  课程1的描述  1
    sleep  2
    ${expectCourses2}  create list  课程1  课程2
    checkCourse  ${expectCourses2}
    [Teardown]  DeleteAllCourse