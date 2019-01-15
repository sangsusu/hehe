from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.weather.com.cn/html/province/jiangsu.shtml")

ele = driver.find_element_by_id("forecastID")

html_doc = ele.get_attribute('innerHTML')

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,"html5lib")

dls = soup.find_all('dl')

citys = []
for dl in dls:
    name = dl.dt.a.string
    ltemp = dl.dd.find('b').string
    ltemp = int(ltemp.replace('℃',''))
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