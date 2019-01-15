from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.example.com")
driver.add_cookie({'name':'key', 'value':'value', 'path':'/'})

for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))