from selenium import webdriver

mobile_emulation = { "deviceName": "Pixel 2" }

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome( desired_capabilities = chrome_options.to_capabilities())

driver.get('http://www.baidu.com')



input()
driver.quit()