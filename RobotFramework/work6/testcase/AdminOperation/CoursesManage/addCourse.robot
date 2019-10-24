*** Settings ***
Resource  rclib/resourse.robot
*** Test Cases ***
addCourse
    [Setup]  deleteCourses
    addCourse  testCourse2  testCourse2的描述  2
    ${expects1}  create list  testCourse2
    courseVerification  ${expects1}
    addCourse   testCourse1  testCourse1的描述  1
    ${expects2}  create list  testCourse1   testCourse2
    courseVerification  ${expects2}
    [Teardown]  deleteCourses