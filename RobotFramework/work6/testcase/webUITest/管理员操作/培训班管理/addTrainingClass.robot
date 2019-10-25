*** Settings ***
Library  SeleniumLibrary
Library  pylib.Resource.WebOpAdmin
*** Test Cases ***
addTrainingClass
    [Setup]  run keywords  DeleteAllCourse
    ...     AND     AddCourse  初中语文  初中语文的描述  1
    ...     AND     AddCourse  初中数学  初中数学描述  2
    ...     AND     DeleteTrainingClass
    ${courses}     create list  初中语文   初中数学
    AddTrainingClass    初中班    初中班的描述     1   ${courses}
    ${expectTrainingClass}  create list  初中班
    checkTrainingClass      ${expectTrainingClass}
    [Teardown]  run keywords    DeleteTrainingClass
    ...     AND     DeleteAllCourse
