*** Settings ***
Library  pylib.WebOpAdmin

*** Test Cases ***

addC1
    [setup]   deleteAllCourse

    add_course    python    python_desc    2
    add_course    python2   python_desc2    1
    ${courses}=    get course list
    should be true    $courses==['python2','python']    #这边判断列表相等，用==

    [teardown]    deleteAllCourse
