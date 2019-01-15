from appium import webdriver
import time,traceback
import winsound
from pylib.input_method import input_method
from appium.webdriver.common.touch_action import TouchAction


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8'
desired_caps['deviceName'] = 'appium-selenium'
# desired_caps['app'] = r'd:\apk\xmmz_debug_4.1.apk'
desired_caps['appPackage'] = 'com.lrlz.beautyshop'
desired_caps['appActivity'] = 'com.lrlz.beautyshop.page.other.SplashActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.implicitly_wait(12)


class keywordlib:

    def login(self,usermobile):

            # 根据id找到元素，并点击，id和 html 元素的id不同
            driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab5").click()
            time.sleep(1)
            driver.find_element_by_id("com.lrlz.beautyshop:id/wave").click()
            time.sleep(1)

            input_method.appium(self)

            # 输入用户名、手动输入验证码
            ele = driver.find_element_by_id("com.lrlz.beautyshop:id/et_phone")
            ele.send_keys(usermobile)
            driver.find_element_by_id("com.lrlz.beautyshop:id/bt_next").click()
            time.sleep(1)

            input_method.huawei(self)

            winsound.Beep(1500, 1000)
            time.sleep(10)

            # 点击登录
            driver.find_element_by_id('com.lrlz.beautyshop:id/btn_login').click()
            # 跳过关联微信
            driver.find_element_by_id('com.lrlz.beautyshop:id/btn_cancel').click()
            time.sleep(2)

            username = driver.find_element_by_id('com.lrlz.beautyshop:id/tv_member_name')
            assert username.text == '久', '登录页面未找到'
            print(f'用户 {username.text} 登陆成功')

            input_method.appium(self)

    def exit(self):

        driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab5").click()
        time.sleep(1)

        driver.find_element_by_id("com.lrlz.beautyshop:id/iv_menu").click()
        time.sleep(1)
        # 点击退出
        driver.find_element_by_id("com.lrlz.beautyshop:id/logout").click()
        time.sleep(1)
        # 点击确定
        driver.find_element_by_id("android:id/button1").click()

        driver.press_keycode(4)

        # username = driver.find_element_by_id('com.lrlz.beautyshop:id/tv_member_name')
        # assert username.text == '登录', '未退出登录'
        # print('成功退出登陆')

    def search(self):

        driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab1").click()
        # time.sleep(1)

        driver.find_element_by_id("com.lrlz.beautyshop:id/search").click()
        # time.sleep(1)

        # 输入兰蔻
        ele = driver.find_element_by_id("com.lrlz.beautyshop:id/et_search_content")
        ele.send_keys('兰蔻')
        # 点击搜索
        driver.find_element_by_id("com.lrlz.beautyshop:id/bt_search").click()
        time.sleep(1)
        ele = driver.find_element_by_id("com.lrlz.beautyshop:id/tv_toolbar_title")
        page_title = ele.text

        assert page_title == '兰蔻','搜索页面不正确'
        print(f'成功搜索关键字{page_title}')

        # driver.press_keycode(4)
        # time.sleep(1)
        # driver.press_keycode(4)
        # time.sleep(1)

    def buy(self):

        # 点击兰蔻第一个商品
        driver.find_elements_by_id("com.lrlz.beautyshop:id/iv_goods_pic")[0].click()

        # 点击购买
        driver.find_element_by_id("com.lrlz.beautyshop:id/tv_buy").click()

        # 点击确定
        driver.find_element_by_id("com.lrlz.beautyshop:id/button").click()
        time.sleep(1)

        driver.find_element_by_id("com.lrlz.beautyshop:id/iv_wxpay_check").click()  # 选择微信支付

        driver.find_element_by_id("com.lrlz.beautyshop:id/pay_btn").click()
        time.sleep(1)

        driver.find_element_by_id("com.tencent.mm:id/jc").click()
        time.sleep(1)

        ele3 = driver.find_element_by_id("com.lrlz.beautyshop:id/btn_second")
        assert ele3.text == '取消订单', '不是待付款页面页面'
        print('成功跳转待付款页面')
        time.sleep(1)

        driver.press_keycode(4)
        time.sleep(1)
        driver.press_keycode(4)
        time.sleep(1)
        driver.press_keycode(4)
        time.sleep(1)
        driver.press_keycode(4)
        time.sleep(1)

        driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab1")

    def Add_goods_to_cart(self):

        # 点击兰蔻第一个商品
        driver.find_elements_by_id("com.lrlz.beautyshop:id/iv_goods_pic")[0].click()

        # 取出商品名称
        goods = driver.find_element_by_id("com.lrlz.beautyshop:id/goodsName")
        goods_name = goods.text
        goods_name = goods_name.strip()
        the_name1 = goods_name.split('150ml')[0]
        print(the_name1)

        # 点击加入购物车
        driver.find_element_by_id("com.lrlz.beautyshop:id/tv_addcart").click()

        # 点击确定
        driver.find_element_by_id("com.lrlz.beautyshop:id/button").click()
        time.sleep(1)

        # 点击购物车图标
        driver.find_element_by_id("com.lrlz.beautyshop:id/cart").click()
        time.sleep(3)

        # 购物车第一个商品的名称
        goods = driver.find_elements_by_id("com.lrlz.beautyshop:id/goodsName")[0]
        goods_name = goods.text
        the_name2 = goods_name.strip()
        print(the_name2)
        time.sleep(2)

        assert the_name1 == the_name2, '商品未成功添加至购物车'
        print('商品已正确添加至购物车')

    def Increase_the_quantity(self):

        driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab4").click()
        time.sleep(1)

        # 商品原来的数量
        num_before = driver.find_elements_by_id("com.lrlz.beautyshop:id/editText")[0]
        num_before = int(num_before.text)
        print(num_before)

        time.sleep(1)

        # 点击购物车商品数量+号
        driver.find_elements_by_id("com.lrlz.beautyshop:id/addBtn")[0].click()
        time.sleep(1)
        driver.find_elements_by_id("com.lrlz.beautyshop:id/addBtn")[0].click()
        time.sleep(3)

        driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab1").click()
        time.sleep(1)
        driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab4").click()
        time.sleep(1)

        # 商品当前的数量
        num_after = driver.find_elements_by_id("com.lrlz.beautyshop:id/editText")[0]
        num_after = int(num_after.text)
        print(num_after)

        assert num_after - num_before == 2,'商品数量没有正确添加'
        print('商品数量正确添加')

    def Reduce_quantity(self):

        driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab1").click()
        time.sleep(1)

        driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab4").click()
        time.sleep(1)

        # 商品原来的数量
        num1 = driver.find_elements_by_id("com.lrlz.beautyshop:id/editText")[0]
        num1 = int(num1.text)
        print(num1)

        time.sleep(1)

        # 点击购物车商品数量-号
        driver.find_elements_by_id("com.lrlz.beautyshop:id/reduceBtn")[0].click()
        time.sleep(1)
        driver.find_elements_by_id("com.lrlz.beautyshop:id/reduceBtn")[0].click()
        time.sleep(3)

        driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab1").click()
        time.sleep(1)
        driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab4").click()
        time.sleep(1)

        # 商品当前的数量
        num2 = driver.find_elements_by_id("com.lrlz.beautyshop:id/editText")[0]
        num2 = int(num2.text)
        print(num2)

        assert num1 - num2 == 2,'商品数量没有正确减少'
        print('商品数量正确减少')

    def delete_cart_goods(self):
        # 删除后定位不了元素，显示一直在刷新加载中，无法后续操作

        time.sleep(2)

        driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab1").click()
        time.sleep(1)
        driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab4").click()
        time.sleep(1)

        # 取出 现在第一个商品的名称
        goods = driver.find_elements_by_id("com.lrlz.beautyshop:id/goodsName")[0]
        goods_name = goods.text
        the_name1 = goods_name.strip()
        print(the_name1)

        # 长按 实现方法:坐标
        TouchAction(driver).long_press(x=660,y=590,duration=2000).perform()
        # 点击确定删除
        driver.find_element_by_id("android:id/button1").click()
        time.sleep(8)

        # 取出 现在第一个商品的名称
        good = driver.find_elements_by_id("com.lrlz.beautyshop:id/goodsName")[0]
        good_name = good.text
        the_name2 = good_name.strip()
        print(the_name2)

        # 确认第一个商品删除成功
        assert the_name1 != the_name2,'商品未成功删除'
        print('商品被成功删除')

        driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab4").click()
        time.sleep(1)

        # # 将数量减为0
        # driver.find_elements_by_id("com.lrlz.beautyshop:id/reduceBtn")[0].click()
        # time.sleep(1)
        # # 点击确定
        # driver.find_element_by_id("android:id/button1").click()
        # time.sleep(3)

        # driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab1").click()
        # time.sleep(1)
        # driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab4").click()
        # time.sleep(1)

    def Not_login_quanquan(self):

        driver.find_element_by_id('com.lrlz.beautyshop:id/rl_main_tab2').click()
        time.sleep(1)

        ele = driver.find_element_by_id('com.lrlz.beautyshop:id/et_phone')
        time.sleep(1)

        assert ele.text == '请输入手机号码 免注册登录','未跳转登录页面'
        print('成功跳转登录页面')

        driver.press_keycode(4)

    def Not_login_Welfare_service(self):

        driver.find_element_by_id('com.lrlz.beautyshop:id/rl_main_tab3').click()
        time.sleep(1)

        ele = driver.find_element_by_id('com.lrlz.beautyshop:id/et_phone')
        time.sleep(1)

        assert ele.text == '请输入手机号码 免注册登录','未跳转登录页面'
        print('成功跳转登录页面')

        driver.press_keycode(4)

    # def Not_login_cart(self):
    # 无法实现，因为有时候跳转登陆界面，有时候不跳转
    #     driver.find_element_by_id('com.lrlz.beautyshop:id/rl_main_tab4').click()
    #     time.sleep(1)
    #
    #     ele = driver.find_element_by_id('com.lrlz.beautyshop:id/et_phone')
    #     time.sleep(1)

    #     assert ele.text == '请输入手机号码 免注册登录','未跳转登录页面'
    #     print('成功跳转登录页面')
    #
    #     driver.press_keycode(4)

    def chat_characters(self, word):

        driver.find_element_by_id('com.lrlz.beautyshop:id/rl_main_tab2').click()
        time.sleep(1)

        driver.find_elements_by_id('com.lrlz.beautyshop:id/stick_mask')[2].click()
        time.sleep(1)

        driver.find_element_by_id('com.lrlz.beautyshop:id/etInput').send_keys(f'{word}')
        time.sleep(1)

        driver.find_element_by_id('com.lrlz.beautyshop:id/btnSend').click()
        time.sleep(1)

        ele = driver.find_elements_by_id('com.lrlz.beautyshop:id/ivMessage')[-1]
        message = ele.text

        assert message == f'{word}', f'没有正确发送 {word}'
        print(f'成功发送 {word} 到群聊')

        driver.press_keycode(4)

    def chat_picture(self):

        driver.find_element_by_id('com.lrlz.beautyshop:id/rl_main_tab2').click()
        time.sleep(1)

        driver.find_elements_by_id('com.lrlz.beautyshop:id/stick_mask')[2].click()
        time.sleep(1)

        # 点击更多+键
        driver.find_element_by_id('com.lrlz.beautyshop:id/ivMore').click()
        time.sleep(1)

        # 点击相册
        driver.find_element_by_id('com.lrlz.beautyshop:id/ivAlbum').click()
        time.sleep(1)

        # 选择第二张照片
        driver.find_elements_by_id('com.lrlz.beautyshop:id/v_selected')[1].click()
        time.sleep(1)

        # 点击完成
        driver.find_element_by_id('com.lrlz.beautyshop:id/done').click()
        time.sleep(1)

        # driver.press_keycode(4)
        # time.sleep(2)

        driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="转到上一层级"]').click()
        time.sleep(1)


