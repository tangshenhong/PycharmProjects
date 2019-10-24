*** Settings ***
Library  SeleniumLibrary
Library  Collections
*** Keywords ***
login
    [Arguments]  ${username}    ${password}
    open browser  http://localhost:8080/mgr/login/login.html     chrome
    set selenium implicit wait  5
    maximize browser window
    input text  css:#username   ${username}
    input text  css:#password   ${password}
    click element  css:button[onclick="postLoginRequest()"]
    sleep  1
addCourse
    [Arguments]  ${courseName}  ${courseDesc}   ${courseSort}
    click element  css:button[ng-click="showAddOne=true"]
    input text  css:[ng-model="addData.name"]   ${courseName}
    input text  css:[ng-model="addData.desc"]   ${courseDesc}
    input text  css:[ng-model="addData.display_idx"]    ${courseSort}
    click element  css:[ng-click="addOne()"]
    sleep  1
checkCourse
    [Arguments]  ${expectCourse}
    ${courseElements}  Get WebElements     css:tr.ng-scope>td:nth-child(2)
    ${courseList}   Create List
    FOR  ${one}  IN  @{courseElements}
        Append To List  ${courseList}   ${one.text}
    END
    run keyword if  $expectCourse==$courseList  log to console  \n测试通过，课程列表为${courseList}
setupAndTearup
    login   auto    sdfsdfsdf
    FOR     ${one}   IN RANGE  10000
        ${deles}    Get WebElements     css:button[ng-click="delOne(one)"
        exit for loop if  ${deles}==[]
        click element  css:tbody>tr:nth-child(1) button[ng-click="delOne(one)"
        sleep  1
        click element  css:button.btn.btn-primary
        sleep  1
    END
    log to console  初始化清除完毕
    close browser


