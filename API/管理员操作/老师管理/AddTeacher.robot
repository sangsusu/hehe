*** Settings ***
Library  pylib.WebOpAdmin


*** Test Cases ***

addT1
    [setup]   run keywords   deleteAllTeacher
    ...    AND    deleteAllCourse
    ...    AND    add_course    初中语文    初中语文描述    1
    ...    AND    add_course    初中数学    初中数学描述    2

    add_teacher    老师B    AAA    laoshi_desc    2    初中语文
    add_teacher    老师A    BBB    laoshi_desc    1    初中数学
    ${teachers}=    get teacher list
    should be true    $teachers==['老师A','老师B']       #这边判断列表相等，用==

    [teardown]    run keywords    deleteAllTeacher   AND   deleteAllCourse