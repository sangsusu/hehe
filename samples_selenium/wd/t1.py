from selenium import webdriver
from selenium.webdriver.support.ui import Select

#如果环境变量path中有路径，可以不用写全
driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
# 别忘了设置
driver.implicitly_wait(10)

# 抓取信息
driver.get('http://www.ahszu.edu.cn/')





fromEle = driver.find_element_by_css_selector('div.nav > ul > li:nth-child(3)')
fromEle.click()

input()

driver.quit()
