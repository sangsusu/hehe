*** Settings ***
Library    pylib.SchoolClassLib


*** Test Cases ***
添加班级2 - tc000002
# 添加 7年级2班
    ${ret1}=    add school class    1     2班     60
    should be true     $ret1['retcode']==0

#列出班级，检验一下
    ${ret2}=    list school class    1
    ${retlist}=   evaluate   $ret2['retlist']
    classlist should contain   ${retlist}
    ...  2班  七年级    &{ret1}[invitecode]   60   0   &{ret1}[id]

    [Teardown]    delete_school_class   &{ret1}[id]


添加班级3 - tc000003

#  添加7年级1班
    ${ret1}=    add school class    1     1班     60
    should be true     $ret1['retcode']==1
    should be true     $ret1['reason']=='duplicated class name'

#列出班级，检验一下
    ${ret2}=    list school class    1

    classlist should not contain   &{ret2}[retlist]
                               ...  1班   七年级
                               ...  &{ret1}[invitecode]
                               ...  60  0  &{ret1}[id]
