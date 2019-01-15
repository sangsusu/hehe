from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.weather.com.cn/html/province/jiangsu.shtml")

ele = driver.find_element_by_id("forecastID")
# print(ele.text)
CitysWeather = ele.text.split("℃\n")

#从forecastID元素获取所有子元素dl
dls = ele.find_elements_by_tag_name('dl')

#将城市和气温信息保存到列表citys中
citys = []
for dl in dls:
    name = dl.find_element_by_tag_name('dt').text
    #最高最低气温位置会变，根据位置决定是span还是b
    ltemp = dl.find_element_by_tag_name('b').text

    ltemp = int(ltemp.replace('℃',''))
    print(name,ltemp)
    citys.append([name,ltemp])

lowest = None
lowestCitys = []
for one in citys :
    curcity = one[0]
    ltemp = one[1]

    if lowest == None or ltemp < lowest:
        lowest = ltemp
        lowestCitys = [curcity]
    elif ltemp == lowest:
        lowestCitys.append(curcity)


print('温度最低有%s℃，城市有%s' % (lowest,' '.join(lowestCitys)))
driver.quit()
