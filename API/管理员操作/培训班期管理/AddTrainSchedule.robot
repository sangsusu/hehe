*** Settings ***
Library  pylib.WebOpAdmin

*** Test Cases ***


addTS
    [setup]   run keywords   deleteAllTrainSchedule
    ...    AND    deleteAllTrainCourse
    ...    AND    deleteAllTeacher
    ...    AND    deleteAllCourse
    ...    AND    add_course    初中语文    初中语文描述    1
    ...    AND    add_course    初中数学    初中数学描述    2
    ...    AND    addTrainCourse    初中班    初中培训班    1    初中语文   初中数学

    addTrainSchedule    初中班1期    desc    1    初中班

    ${Schedules}=     get Schedule list
    should be true    $Schedules==['初中班1期']
    [teardown]   run keywords   deleteAllTrainSchedule   AND    deleteAllTrainCourse    AND    deleteAllTeacher    AND   deleteAllCourse
