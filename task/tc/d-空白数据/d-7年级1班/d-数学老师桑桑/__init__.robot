*** Settings ***
Library    pylib.TeacherLib
Variables   cfg.py

Suite Setup      add teacher    sangsang   桑桑
               ...    ${g_subject_math_id}
               ...    ${suite_g7c1_classid}
               ...    13900000000    13900000000@qq.com    13900000000
               ...    suite_math_teacher_id


Suite Teardown   delete_teacher    ${suite_math_teacher_id}



