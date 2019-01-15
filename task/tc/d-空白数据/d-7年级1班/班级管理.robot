*** Settings ***
Library    pylib.SchoolClassLib
Variables   cfg.py

*** Test Cases ***

添加班级2 - tc000002

    ${ret1}=    add school class    ${g_grade_7_id}    2班    60
    should be true    $ret1['retcode']==0

    ${ret2}=    list school class    ${g_grade_7_id}
    ${retlist}=  evaluate  $ret2['retlist']

    classlist should contain  ${retlist}  七年级  &{ret1}[id]  &{ret1}[invitecode]   2班  60  0

    [teardown]    delete school class    &{ret1}[id]




添加班级3 - tc000003

    ${listBefore}=    list school class    ${g_grade_7_id}

    ${Addret}=    add school class    ${g_grade_7_id}    1班    60
    should be true    $Addret['retcode']==1
    should be true    $Addret['reason']=="duplicated class name"

    ${listAfter}=    list school class    ${g_grade_7_id}

    should be true    $listBefore==$listAfter

    #该用例存在系统bug，会执行失败



修改班级1 - tc000051

    ${ret1}=    add school class    ${g_grade_7_id}    2班    60
    should be true    $ret1['retcode']==0
    ${classid}=    evaluate    $ret1['id']

    ${modifyret}=    modify school class    ${classid}    5班    80
    should be true    $modifyret['retcode']==0

    ${ret2}=    list school class    ${g_grade_7_id}
    ${retlist}=    evaluate    $ret2['retlist']

    classlist should contain    ${retlist}
    ...    七年级    &{ret1}[id]    &{ret1}[invitecode]    5班    80    0

    [teardown]    delete school class    &{ret1}[id]



修改班级2 - tc000052

    ${ret1}=    add school class    ${g_grade_7_id}    2班    60
    should be true    $ret1['retcode']==0
    ${classid}=    evaluate    $ret1['id']

    ${listret1}=    list school class    ${g_grade_7_id}

    ${modifyret}=    modify school class    ${classid}    1班    60
    should be true    $modifyret['retcode']==1
    should be true    $modifyret['reason']=='duplicated class name'

    ${listret2}=    list school class    ${g_grade_7_id}

    should be equal    ${listret1}    ${listret2}

    [teardown]    delete school class     ${classid}

    #该用例存在系统bug，会执行失败



修改班级3 - tc000053

    ${modifyRet}=    modify school class    9999999999    1班    60
    should be true    $modifyRet['retcode']==404
    should be true    $modifyret['reason']=="id 为`9999999999`的班级不存在"



删除班级1 - tc000081

    ${delRet}=    delete school class   9999999999
    should be true    $delRet['retcode']==404
    should be true    $delRet['reason']=="id 为`9999999999`的班级不存在"



删除班级2 - tc000082

    ${listbefore}=    list school class    ${g_grade_7_id}
    ${ret1}=    add school class    ${g_grade_7_id}    2班    60
    should be true    $ret1['retcode']==0
    ${classid}=    evaluate    $ret1['id']

    ${delret}=    delete school class    ${classid}
    should be true    $delret['retcode']==0

    ${listafter}=    list school class    ${g_grade_7_id}

    should be equal    ${listbefore}    ${listafter}



















