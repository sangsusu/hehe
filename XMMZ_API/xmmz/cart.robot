*** Settings ***
Library   pylibnew.cartlib
Variables  cfgnew.py

*** Test Cases ***
add-00001
    ${ret}=    login    13900000000    1111
    should be true    $ret['code']==200


