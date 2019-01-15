*** Settings ***
Library  pylib.WebOpAdmin

*** Test Cases ***

# 前置条件：系统中还没有培训班，已经有课程 ‘初中语文’，‘初中数学’
# step 1： 添加培训班，输入培训班名（初中班）、详情描述、展示次序为1，包含课程为初中语文’和‘初中数学’，点击创建
# 预期结果：创建的培训班正确显示在下面的表中。

addTC
    [setup]   run keywords   deleteAllTrainCourse
    ...    AND    deleteAllTeacher
    ...    AND    deleteAllCourse
    ...    AND    add_course    初中语文    初中语文描述    1
    ...    AND    add_course    初中数学    初中数学描述    2

    addTrainCourse    初中班    初中培训班    1     初中语文   初中数学

    ${courses}=    get Train Course list
    should be true    $courses==['初中班']
    [teardown]    run keywords    deleteAllTrainCourse    AND    deleteAllTeacher   AND   deleteAllCourse