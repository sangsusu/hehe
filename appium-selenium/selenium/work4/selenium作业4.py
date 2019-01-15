from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('http://www.51job.com')

driver.find_element_by_class_name('more').click()
driver.find_element_by_id('kwdselectid').send_keys('python')
driver.find_element_by_id('work_position_click').click()
#这边睡一下是为了防止前端定位地址还没有定位到
time.sleep(1)
selectedCityEles = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em[class=on]')
for one in selectedCityEles:
    one.click()
    time.sleep(1)
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()
driver.find_element_by_id('work_position_click_bottom_save').click()
time.sleep(1)
# 要点一下别的地方， 否则下面的元素会被挡住
driver.find_element_by_css_selector('div.tit').click()
driver.find_element_by_id('funtype_click').click()
driver.find_element_by_id('funtype_click_center_left_each_0100').click()
driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()
driver.find_element_by_id('funtype_click_bottom_save').click()

driver.find_element_by_css_selector('#cottype_list .ic').click()
driver.find_element_by_css_selector("span[title='外资（欧美）']").click()
driver.find_element_by_css_selector('#workyear_list .ic').click()
driver.find_element_by_css_selector(".ul span[title='1-3年']").click()
driver.find_element_by_css_selector('.btnbox .p_but').click()

messages = driver.find_elements_by_css_selector("#resultList div[class='el']")
for message in messages:
    fields = message.find_elements_by_tag_name('span')
    stringFilelds = [field.text for field in fields]
    print(' | '.join(stringFilelds))
driver.quit()
