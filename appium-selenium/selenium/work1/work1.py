from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.weather.com.cn/html/province/jiangsu.shtml")

weather_Info = driver.find_element_by_id("forecastID")
# print(weather_Info.text)
Info = weather_Info.text.split("℃\n")
# print(Info)
Infodic = {}
for one in Info:
    one = one.replace('℃','')
    useInfo = one.split("/")
    name = useInfo[0].split("\n")[0].replace("'","").strip()
    weath = useInfo[1].replace("'","").strip()
    weath = int(weath)
    Infodic.update({name:weath})
print(Infodic)
lowest = 50
lowestCity = []
for key,value in Infodic.items():
    if value < lowest:
        lowest = value
        lowestCity = [key]
    elif value == lowest:
        lowestCity.append(key)
print('最低气温是：%d℃,城市有:%s' % (lowest,' '.join(lowestCity)))


