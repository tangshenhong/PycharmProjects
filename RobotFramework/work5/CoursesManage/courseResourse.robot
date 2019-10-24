*** Settings ***
Library  SeleniumLibrary
Library  Collections
*** Keywords ***
deleteCourses
    set browser implicit wait  2
    click element  css:[href="#/"]
    sleep  1
    FOR  ${one}  IN RANGE  1000
        ${deleteButtons}  SeleniumLibrary.Get WebElements  css:button[ng-click="delOne(one)"]
        Exit For Loop If    $deleteButtons==[]
        Click Element     ${deleteButtons[0]}
        Click Element   css:button.btn.btn-primary
        sleep  1
    END
    set browser implicit wait  10
addCourse
    [Arguments]  ${courseName}  ${courseDesc}  ${order}
    Click Element  css:button[ng-click="showAddOne=true"]
    Input Text  css:[ng-model="addData.name"]  ${courseName}
    Input Text  css:[ng-model="addData.desc"]  ${courseDesc}
    Input Text  css:[ng-model="addData.display_idx"]  ${order}
    Click Element  css:[ng-click="addOne()"]
    sleep  1
courseVerification
    [Arguments]  ${expects}
    ${realElements}  SeleniumLibrary.Get WebElements  css:tbody>tr>td:nth-child(2) span
    ${reals}    create list
    FOR  ${one}  IN  @{realElements}
        append to list  ${reals}    ${one.text}
    END
    should be equal  ${expects}  ${reals}
