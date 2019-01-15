*** Settings ***
Library    pylib.StudentLib
Variables   cfg.py

*** Test Cases ***
添加学生2 - tc002002

    # 添加学生2到7年级1班
    ${addRet}    add student    luxun    陆逊
          ...    ${g_grade_7_id}
          ...    ${suite_g7c1_classid}
          ...    13900000002

    should be true    $addRet['retcode']==0   # python表达式

    ${listRet}=    list student

    studentlist should contain    &{listRet}[retlist]
    ...    luxun    陆逊    &{addRet}[id]   # rf写法
    ...    13900000002    ${suite_g7c1_classid}

    [Teardown]    delete student    &{addRet}[id]



添加学生3 - tc002003

    ${listbefore}=    list student

    ${addRet}    add student    luxun    陆逊
          ...    ${g_grade_7_id}
          ...    ${suite_g7c1_classid}
          ...    13900000002

    should be true    $addRet['retcode']==0   # python表达式

    ${delRet}=    delete_student    &{addRet}[id]
    should be true    $delRet['retcode']==0

    ${listafter}=    list student

   should be true    ${listbefore}==${listafter}


