from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.weather.com.cn/html/province/jiangsu.shtml")

weather_Info = driver.find_element_by_id("forecastID")
# print(weather_Info.text)
CitysWeather = weather_Info.text.split("℃\n")

lowest = None
lowestCitys = []
for one in CitysWeather :
    one = one.replace('℃','')
    curcity = one.split('\n')[0]
    lowweather = int(one.split('/')[1])

    if lowest == None or lowweather < lowest:
        lowest = lowweather
        lowestCitys = [curcity]
    elif lowweather == lowest:
        lowestCitys.append(curcity)

print('温度最低有%s℃，城市有%s' % (lowest, ' '.join(lowestCitys)))
driver.quit()