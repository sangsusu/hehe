*** Keywords ***
suit setup action
    ${ret}    add school class    ${g_grade_7_id}    1班    60
    set global variable    ${suite_g7c1_classid}    &{ret}[id]


*** Settings ***
Library    pylib.SchoolClassLib
Variables   cfg.py

Suite Setup      suit setup action
Suite Teardown   delete_school_class    ${suite_g7c1_classid}



