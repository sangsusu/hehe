*** Settings ***
Library    pylib.TeacherLib
Library    pylib.StudentLib
Library    pylib.WebOpLib
Variables   cfg.py

Suite Setup    open browser
Suite Teardown    close browser

*** Test Cases ***
老师登陆2 - tc005002

    ${addRet}=     add teacher    liusheng    刘生
            ...    ${g_subject_math_id}
            ...    ${suite_g7c1_classid}
            ...    13900000011    13900000011@qq.com    13900000011

    should be true    $addRet['retcode']==0

    teacher_login    liusheng    888888

    ${homepage_info}    get_teacher_homepage_info

    should be true    $homepage_info==['松勤学院0221','刘生','初中数学','0','0','0']

    ${students_info}    get_teacher_class_students_info

    should be true    $students_info=={'七年级1班':['孙权']}

    [Teardown]    delete teacher    &{addRet}[id]















