*** Settings ***
Resource  Resource1.robot
*** Test Cases ***
addCourse
    [Setup]  setupAndTearup
    login   auto    sdfsdfsdf
    #步骤 1： 添加课程，输入课程名、详情描述、展示次序为2，点击创建
         #预期结果：创建的课程正确显示在下面的表中。
    addCourse   测试课程2    测试课程2的描述  2
    ${expectCourse1}  Create List  测试课程2
    checkCourse  ${expectCourse1}
    #步骤 2： 再添加一门课程，输入课程名、详情描述、展示次序为1，点击创建
         #预期结果：创建的课程正确显示在下面的表中，并且按照展示次序排列。
    addCourse   测试课程1    测试课程1的描述  1
    ${expectCourse2}  Create List  测试课程1  测试课程2
    checkCourse  ${expectCourse2}
    close browser
    [Teardown]  setupAndTearup