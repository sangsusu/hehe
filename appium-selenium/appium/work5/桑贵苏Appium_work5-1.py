from appium import webdriver
import traceback


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7'
desired_caps['deviceName'] = 'appium-selenium'

desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    driver.implicitly_wait(10)

    javaCode = 'new UiSelector().resourceId("io.manong.developerdaily:id/tv_title").instance(0)'
    title1 = driver.find_element_by_android_uiautomator(javaCode)
    title1.click()
    Thetitle1 = title1.text

    title2 = driver.find_element_by_id('io.manong.developerdaily:id/tv_title')
    Thetitle2 = title2.text

    assert Thetitle1 == Thetitle2,'fail'
    print('pass')

    driver.press_keycode(4)

    javaCode = 'new UiSelector().resourceId("io.manong.developerdaily:id/tv_tab_title").instance(0)'
    name = driver.find_element_by_android_uiautomator(javaCode)
    if name.text == '精选':
        print("已返回首页")


except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()