*** Settings ***
Library  SeleniumLibrary
*** Test Cases ***
hotsellcase
    open browser      https://www.vmall.com/index.html     chrome
    set browser implicit wait  10
    ${hots}    Get WebElements     css:.span-968.fl .grid-title
    FOR     ${hot}  IN   @{hots}
        log to console      ${hot.text}
    END
    close browser
