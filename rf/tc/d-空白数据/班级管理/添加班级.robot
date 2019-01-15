*** Settings ***
Library    pylib.SchoolClassLib

*** Test Cases ***

添加班级1 - tc000001

    ${addret}=    add school class    1    1班    60
    should be true    $addret['retcode']==0
    ${listret}=    list school class    1

    ${fc}=    evaluate    $listret['retlist'][0]
    should be true    $fc['id']==$addret['id']
    should be true    $fc['invitecode']==$addret['invitecode']
    should be true    $fc['grade__name']=='七年级'
    should be true    $fc['studentlimit']==60
    should be true    $fc['name']=='1班'

    [teardown]    delete school class    &{addret}[id]    #取出id用rf写法，&符号