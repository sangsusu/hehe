from appium import webdriver
import time,traceback

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7'
desired_caps['deviceName'] = 'appium-selenium'
#desired_caps['app'] = r'f:\apk\duoduoCalculators.apk'
desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity'] = 'com.ibox.calculators.SplashActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    driver.implicitly_wait(10)

    # driver.find_element_by_id("com.ibox.calculators: id / update_id_cancel").click()
    # time.sleep(2)

    driver.find_element_by_id("com.ibox.calculators:id/digit3").click()

    driver.find_element_by_id("com.ibox.calculators:id/plus").click()

    driver.find_element_by_id("com.ibox.calculators:id/digit9").click()

    driver.find_element_by_id("com.ibox.calculators:id/equal").click()

    driver.find_element_by_id("com.ibox.calculators:id/mul").click()

    driver.find_element_by_id("com.ibox.calculators:id/digit5").click()

    driver.find_element_by_id("com.ibox.calculators:id/equal").click()


    num = driver.find_element_by_id("com.ibox.calculators:id/cv")
    Thenum = num.find_elements_by_class_name('android.widget.TextView')
    # for one in Thenum:
    #     print(one.text)
    correct_num = int(Thenum[1].text)
    if correct_num == 60:
        print('结果正确')

except:
    print (traceback.format_exc())

driver.quit()