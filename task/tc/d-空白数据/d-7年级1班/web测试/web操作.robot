*** Settings ***
Library    pylib.TeacherLib
Library    pylib.StudentLib
Library    pylib.WebOpLib
Variables   cfg.py

*** Test Cases ***
老师登陆1 - tc005001

    ${addRet}=     add teacher    liusheng    刘生
            ...    ${g_subject_math_id}
            ...    ${suite_g7c1_classid}
            ...    13900000011    13900000011@qq.com    13900000011

    should be true    $addRet['retcode']==0

    teacher_login    liusheng    888888

    ${homepage_info}    get_teacher_homepage_info

    should be true    $homepage_info==['松勤学院0221','刘生','初中数学','0','0','0']

    ${students_info}    get_teacher_class_students_info

    should be true    $students_info=={'七年级1班':[]}

    [Teardown]    delete teacher    &{addRet}[id]



学生登录1 - tc005081

    ${addRet}    add student    zhangfei    张飞
          ...    ${g_grade_7_id}
          ...    ${suite_g7c1_classid}
          ...    13900000003

    should be true    $addRet['retcode']==0

    student_login    zhangfei    888888

    ${homepage_info}    get_student_homepage_info

    should be true    $homepage_info==['张飞', '松勤学院0221', '0', '0']

    ${error_info}    student_error_bank

    should be true    $error_info=='您尚未有错题入库哦'

    [Teardown]    delete student    &{addRet}[id]



















