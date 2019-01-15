*** Settings ***
Library    pylib.WebOpLib
Variables   cfg.py

Suite Setup    open browser
Suite Teardown    close browser

*** Test Cases ***
老师发布作业1 - tc005101

    teacher_login    sangsang    888888
    teacher_create_task    test005

    student login    sangsang1    888888
    student do exam

    teacher login    sangsang    888888
    ${choices}=    teacher_check_exam

    should be true    $choices==['B','B','B']



















