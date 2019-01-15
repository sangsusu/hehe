*** Settings ***
Library    pylib.StudentLib
Variables   cfg.py

Suite Setup      add student    sunquan    孙权
               ...    ${g_grade_7_id}
               ...    ${suite_g7c1_classid}
               ...    13900000022
               ...    suite_student_id


Suite Teardown   delete student    ${suite_student_id}



