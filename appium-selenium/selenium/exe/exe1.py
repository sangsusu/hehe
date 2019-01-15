from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('http://a.lrlz.com/mshop/main/mine')

time.sleep(2)

driver.find_elements_by_css_selector('.weui-cell__hd img')[0].click()

driver.find_element_by_css_selector("#app input[name='userMobile']").send_keys('13900000000')
driver.find_element_by_css_selector("#app input[name='code']").send_keys('1111')
# 点击登录
driver.find_element_by_css_selector("#app button.button_submit").click()

time.sleep(2)
# 点击 购物车tab
driver.find_elements_by_css_selector("#router_view .weui-tabbar a")[2].click()

# 当前第一件商品名称
goods = driver.find_elements_by_css_selector('#router_view div.goods_name p')[0]
goods_name = goods.text
the_name1 = goods_name.strip()
print(the_name1)

time.sleep(2)
# 点击-号
driver.find_elements_by_css_selector("#router_view div.handle span[class='handle_btn minus']")[0].click()
# 确定删除
driver.find_element_by_css_selector("div .weui-dialog__ft a.weui-dialog__btn_primary").click()

time.sleep(2)

# 此时第一件商品名称
goods = driver.find_elements_by_css_selector('#router_view div.goods_name p')[0]
goods_name = goods.text
the_name2 = goods_name.strip()
print(the_name2)

assert the_name1 != the_name2, '商品未成功删除'
print('商品被成功删除')