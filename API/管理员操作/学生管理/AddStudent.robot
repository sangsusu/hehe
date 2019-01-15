*** Settings ***
Library  pylib.WebOpAdmin


*** Test Cases ***

addS1
    [setup]   run keywords   deletStudent
    ...    AND    deleteAllTrainSchedule
    ...    AND    deleteAllTrainCourse
    ...    AND    deleteAllTeacher
    ...    AND    deleteAllCourse
    ...    AND    add_course    初中语文    初中语文描述    1
    ...    AND    add_course    初中数学    初中数学描述    2
    ...    AND    add_teacher    孔子    kongzi    孔子老师    1    初中语文
    ...    AND    add_teacher    庄子    zhuangzi    庄子老师    1    初中数学
    ...    AND    addTrainCourse    初中班    初中培训班    1    初中语文   初中数学
    ...    AND    addTrainSchedule    初中班1期    desc    1    初中班

    addStudent    关羽    guanyu    关羽desc    初中班    初中班1期
    addStudent    张飞    zhangfei    张飞desc    初中班    初中班1期
    ${students}=    getStudentlist
    should be true    $students==['张飞','关羽']       #这边判断列表相等，用==

    [teardown]    run keywords    deletStudent  AND  deleteAllTrainSchedule  AND  deleteAllTrainCourse  AND  deleteAllTeacher   AND   deleteAllCourse