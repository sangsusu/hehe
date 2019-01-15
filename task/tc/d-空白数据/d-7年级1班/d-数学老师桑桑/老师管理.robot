*** Settings ***
Library    pylib.TeacherLib
Library    pylib.SchoolClassLib
Variables   cfg.py

*** Test Cases ***
添加老师2 - tc001002

    ${addRet}=     add teacher    murongchui    慕容垂
             ...    ${g_subject_science_id}
             ...    ${suite_g7c1_classid}
             ...    13900000002    13900000002@qq.com    13900000002

    should be true    $addRet['retcode']==0

    ${listRet}=    list teacher
    teacherlist should contain    &{listRet}[retlist]
              ...    murongchui    慕容垂    &{addRet}[id]
              ...    ${suite_g7c1_classid}
              ...    13900000002    13900000002@qq.com    13900000002

    [Teardown]    delete teacher    &{addRet}[id]



添加老师3 - tc001003

    ${listRet1}=    list teacher

     ${addRet}=     add teacher    sangsang   桑桑
             ...    ${g_subject_math_id}
             ...    ${suite_g7c1_classid}
             ...    13900000000    13900000000@qq.com    13900000000

    should be true    $addRet['retcode']==1
    should be true    $addRet['reason']== "登录名 sangsang 已经存在"

    ${listRet2}=    list teacher

    should be equal    ${listRet1}    ${listRet2}



修改老师1 - tc001051

    ${modifyRet}=    modify_teacher    9999999999
    should be true    $modifyRet['retcode']==1
    should be true    $modifyret['reason']=="id 为`9999999999`的老师不存在"



修改老师2 - tc001052

    ${addclass1}=    add school class    ${g_grade_7_id}    7班    80
    ${classid1}=    evaluate    ${addclass1}['id']

    ${addclass2}=    add school class    ${g_grade_7_id}    8班    80
    ${classid2}=    evaluate    ${addclass2}['id']

    ${addRet}=    add_teacher   yuxia    俞霞    5    ${classid1}    13912345678    13912345678@qq.com    321027199210298888
    should be true    $addRet['retcode']==0
    ${teacherid}=    evaluate    $addRet['id']

    ${modifyret}=    modify_teacher    ${teacherid}    俞霞new    5    ${classid1},${classid2}    13912345678    13912345678@qq.com    321027199210298888
    should be true    $modifyret['retcode']==0

    ${listret}=    list_teacher    5
    ${retlist}=    evaluate    $listret['retlist']

    teacherlist_should_contain    ${retlist}
    ...    yuxia    俞霞new    ${teacherid}    ${classid1},${classid2}    13912345678    13912345678@qq.com    321027199210298888

    [Teardown]     run keywords    delete_teacher    ${teacherid}
                  ...    AND   delete school class    ${classid1}
                  ...    AND   delete school class    ${classid2}



删除老师1 - tc001081

    ${delRet}=    delete_teacher   9999999999
    should be true    $delRet['retcode']==404
    should be true    $delRet['reason']=="id 为`9999999999`的老师不存在"



删除老师2 - tc001082

    ${listret1}=    list_teacher
    ${addclass1}=    add school class    ${g_grade_7_id}    7班    80
    ${classid1}=    evaluate    ${addclass1}['id']

    ${addRet}=    add_teacher   yuxia    俞霞    5    ${classid1}    13912345678    13912345678@qq.com    321027199210298888
    should be true    $addRet['retcode']==0
    ${teacherid}=    evaluate    $addRet['id']

    ${delRet}=    delete_teacher    ${teacherid}
    should be true    $delRet['retcode']==0

    ${listret2}=    list_teacher

    should be equal    ${listret1}    ${listret2}

    [Teardown]     delete school class    ${classid1}
















