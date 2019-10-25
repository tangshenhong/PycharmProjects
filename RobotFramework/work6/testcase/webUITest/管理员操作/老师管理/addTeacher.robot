*** Settings ***
Library  SeleniumLibrary
Library  pylib.Resource.WebOpAdmin
*** Test Cases ***
addTeacher
    [Setup]  run keywords   DeleteAllCourse
    ...     AND     AddCourse  初中语文  初中语文的描述  1
    ...     AND     AddCourse  初中数学  初中数学描述  2
    ...     AND     DeleteAllTeacher
    AddTeacher    老师2  登录2  老师2的描述  2  初中语文
    sleep   2
    ${expectTeachers1}   create list  老师2
    checkTeacher    ${expectTeachers1}
    AddTeacher    老师1  登录1  老师1的描述  1  初中数学
    sleep   2
    ${expectTeachers2}   create list  老师1   老师2
    checkTeacher    ${expectTeachers2}
    [Teardown]  run keywords  DeleteAllTeacher
    ...     AND     DeleteAllCourse
