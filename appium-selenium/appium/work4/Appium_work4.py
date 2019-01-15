from appium import webdriver
import time
import time,traceback

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7'
desired_caps['deviceName'] = 'appium-selenium'
desired_caps['appPackage'] = 'com.huawei.appmarket'
desired_caps['appActivity'] = 'com.huawei.appmarket.MainActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

try:

    javaCode = 'new UiSelector().resourceId("com.huawei.appmarket:id/tabLayout").childSelector(new UiSelector().text("排行"))'

    driver.find_element_by_android_uiautomator(javaCode).click()

    javaCode = 'new UiSelector().text("总榜").resourceId("com.huawei.appmarket:id/ItemTitle")'
    ele = driver.find_element_by_android_uiautomator(javaCode)
    GenerallistX = ele.location['x']
    GenerallistY = ele.location['y']

    driver.implicitly_wait(0.5)
    while True:
        driver.swipe(GenerallistX,GenerallistY,GenerallistX,GenerallistY-120, 300)
        javaCode = 'new UiSelector().text("口碑最佳").resourceId("com.huawei.appmarket:id/ItemTitle")'
        eles1 = driver.find_elements_by_android_uiautomator(javaCode)

        javaCode = 'new UiSelector().text("热门流行游戏").resourceId("com.huawei.appmarket:id/ItemTitle")'
        eles2 = driver.find_elements_by_android_uiautomator(javaCode)
        if eles1 and eles2:
            break

    driver.implicitly_wait(10)
    eles = driver.find_elements_by_class_name("android.widget.TextView")
    namelist = []
    for ele in eles:
        namelist.append(ele.text)

    nameStr = ' '.join(namelist)

    target = nameStr.split('1')[3].split('2')
    target1 = target[0].strip()
    target2 = target[3].strip()
    target3 = target[5].split('3')[1].replace('4','').strip()
    target4 = target[5].split('4')[2].strip()
    target5 = target[6].split('5')[1].strip()
    targetlist = [target1,target2,target3,target4,target5]
    for one in targetlist:
        print(one)


except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()