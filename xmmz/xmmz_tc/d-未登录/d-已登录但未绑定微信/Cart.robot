*** Settings ***
Library    pylib.keywordlib
Variables   cfg2.py

*** Test Cases ***

购物车添加商品 - tc20001

    search
    Add_goods_to_cart


购物车增加商品数量 - tc20002

    Increase_the_quantity


购物车减少商品数量 - tc20003

    Reduce_quantity


#购物车删除商品 - tc20004
#
#    delete_cart_goods
