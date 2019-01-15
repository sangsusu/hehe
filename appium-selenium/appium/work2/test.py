from appium import webdriver
import time,traceback
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


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
    driver.implicitly_wait(10)
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
    TouchAction(driver).long_press(x=660, y=590, duration=2000).perform()
    # 点击确定删除
    driver.find_element_by_id("android:id/button1").click()
    time.sleep(120)

    # 取出 现在第一个商品的名称
    good = driver.find_elements_by_id("com.lrlz.beautyshop:id/goodsName")[0]
    good_name = good.text
    the_name2 = good_name.strip()
    print(the_name2)

except:
    print (traceback.format_exc())