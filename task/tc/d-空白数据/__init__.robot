*** Settings ***
Library    pylib.SchoolClassLib
Library    pylib.TeacherLib
Library    pylib.StudentLib

Suite Setup      Run Keywords    delete_all_teachers    AND
                   ...    delete_all_students    AND
                   ...    delete_all_school_classes

