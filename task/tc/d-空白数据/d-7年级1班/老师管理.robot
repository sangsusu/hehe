*** Settings ***
Library    pylib.TeacherLib
Variables   cfg.py

*** Test Cases ***
添加老师1 - tc001001

    ${addRet}=     add teacher    tuobahong    拓跋宏
             ...    ${g_subject_math_id}
             ...    ${suite_g7c1_classid}
             ...    13900000000    13900000000@qq.com    13900000000

    should be true    $addRet['retcode']==0

    ${listRet}=    list teacher
    teacherlist should contain    &{listRet}[retlist]
              ...    tuobahong    拓跋宏    &{addRet}[id]
              ...    ${suite_g7c1_classid}
              ...    13900000000    13900000000@qq.com    13900000000

    [Teardown]    delete teacher    &{addRet}[id]