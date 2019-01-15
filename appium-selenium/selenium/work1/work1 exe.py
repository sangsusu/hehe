from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("http://www.weather.com.cn/html/province/jiangsu.shtml")

messages = driver.find_elements_by_css_selector("#forecastID>dl")
weaInfo = []
for message in messages:
    city = message.find_element_by_css_selector("dt>a").text
    lowweather = int(message.find_element_by_css_selector("dd>a>b").text.replace('℃',''))
    weaInfo.append([city,lowweather])
# print(weaInfo)
lowest = 100
lowestCity = []
for one in weaInfo:
    lowcity = one[0]
    lowweath = one[1]
    if lowweath < lowest:
        lowest = lowweath
        lowestCity = [lowcity]
    else:
        if lowweath == lowest:
            lowestCity.append(lowcity)
print('最低气温是：%s℃,城市是：%s' % (lowest,' '.join(lowestCity)))

driver.quit()

