*** Settings ***
Library  course_mgr.py
*** Test Cases ***
course_mgr
    ${courses}  list_course
    FOR     ${course}   IN      @{courses}
        log to console  ${course}
    END
    ${predictions}  create list  课程1    课程2     课程3     课程4
    should be equal  ${courses}     ${predictions}


