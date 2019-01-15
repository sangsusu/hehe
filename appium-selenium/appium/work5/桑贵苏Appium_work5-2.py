from appium import webdriver
import time,traceback


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7'
desired_caps['deviceName'] = 'appium-selenium'

desired_caps['appPackage'] = 'com.example.jcy.wvtest'
desired_caps['appActivity'] = 'com.example.jcy.wvtest.MainActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    driver.implicitly_wait(10)
    time.sleep(3)

    print(driver.contexts)




except:
    print (traceback.format_exc())

# input('**** Press to quit..')
# driver.quit()