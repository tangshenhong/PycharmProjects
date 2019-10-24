*** Settings ***
Library  SeleniumLibrary
Variables  variable.py
*** Keywords ***
login
    go to  ${url}
    input text  id:username     ${username}
    input text  id:password     ${password}
    click element  css:[onclick="postLoginRequest()"]
    sleep  1
setupBrower
    open browser  ${url}    Chrome
    maximize browser window
    set browser implicit wait  10
    login
closeProcess
    close browser
