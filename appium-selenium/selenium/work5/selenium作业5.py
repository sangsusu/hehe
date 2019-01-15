from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

input1 = driver.find_element_by_id('fromStationText')
input1.click()
input1.clear()
input1.send_keys('南京南\n')

input2 = driver.find_element_by_id('toStationText')
input2.click()
input2.clear()
input2.send_keys('杭州东\n')

select = Select(driver.find_element_by_id('cc_start_time'))
select.select_by_visible_text('06:00--12:00')

driver.find_element_by_css_selector('#date_range li:nth-child(2)').click()

trainlists = driver.find_elements_by_xpath("//div[@id='t-list']//tbody/tr[@class]/td[4][@class]/../td[1]//a")
for train  in trainlists:
    print (train.text)

driver.quit()
