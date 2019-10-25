*** Settings ***
Library  SeleniumLibrary
Library  pylib.Resource.WebOpAdmin
*** Test Cases ***
addTrainingClassPeriod
    [Setup]  run keywords  DeleteAllCourse
    ...     AND     AddCourse  初中语文  初中语文的描述  1
    ...     AND     AddCourse  初中数学  初中数学描述  2
    ...     AND     DeleteTrainingClass
    ${courses}     create list  初中语文   初中数学
    AddTrainingClass    初中班    初中班的描述     1   ${courses}
    AddTrainingClassPeriod      初中班1期   初中班1期的描述    1   初中班
    ${expectTrainingClassPeriod}    create list  初中班1期
    checkTrainingClassPeriod    ${expectTrainingClassPeriod}
    [Teardown]  run keywords    DeleteTrainingClassPeriod
    ...     AND     DeleteTrainingClass
    ...     AND     DeleteAllCourse
