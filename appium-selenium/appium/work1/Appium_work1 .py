from appium import webdriver
import time,traceback
import winsound


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8'
desired_caps['deviceName'] = 'appium-selenium'
#desired_caps['app'] = r'd:\apk\xmmz_debug_4.1.apk'
desired_caps['appPackage'] = 'com.lrlz.beautyshop'
desired_caps['appActivity'] = 'com.lrlz.beautyshop.page.other.SplashActivity'  # com.lrlz.beautyshop.page.other.SplashActivity  com.github.moduth.blockcanary.ui.DisplayActivity
desired_caps['unicodeKeyboard']  = True
desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    driver.implicitly_wait(3)

    # 根据id找到元素，并点击，id和 html 元素的id不同
    driver.find_element_by_id("com.lrlz.beautyshop:id/iv_main_tab5").click()
    time.sleep(1)
    driver.find_element_by_id("com.lrlz.beautyshop:id/wave").click()
    time.sleep(1)

    # 输入用户名、密码
    ele = driver.find_element_by_id("com.lrlz.beautyshop:id/et_phone")
    ele.send_keys('13900000000')
    driver.find_element_by_id("com.lrlz.beautyshop:id/bt_next").click()
    time.sleep(1)

    winsound.Beep(1500,3000)
    time.sleep(10)

    # 点击登录
    driver.find_element_by_id('com.lrlz.beautyshop:id/btn_login').click()
    #跳过关联微信
    driver.find_element_by_id('com.lrlz.beautyshop:id/btn_cancel').click()
    time.sleep(2)

    username = driver.find_element_by_id('com.lrlz.beautyshop:id/tv_member_name')
    assert username.text == '久','登录页面未找到'
    print(f'用户 {username.text} 登陆成功')


except:
    print (traceback.format_exc())


# input('**** Press to quit..')     #显示后按enter键，退出进程
# driver.quit()