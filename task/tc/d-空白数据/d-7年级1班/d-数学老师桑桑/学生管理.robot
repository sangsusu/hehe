*** Settings ***
Library    pylib.StudentLib
Variables   cfg.py

*** Test Cases ***
添加学生1 - tc002001

    # 添加学生到7年级1班
    ${addRet}    add student    xiahoudun    夏侯惇
          ...    ${g_grade_7_id}
          ...    ${suite_g7c1_classid}
          ...    13900000001

    should be true    $addRet['retcode']==0   # python表达式

    ${listRet}=    list student

    studentlist should contain    &{listRet}[retlist]
    ...    xiahoudun    夏侯惇    &{addRet}[id]   # rf写法
    ...    13900000001    ${suite_g7c1_classid}

    [Teardown]    delete student    &{addRet}[id]




