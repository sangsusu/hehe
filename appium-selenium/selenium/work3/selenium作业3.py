from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://www.51job.com")

mess1 = driver.find_element_by_id('kwdselectid').send_keys('python')
mess2 = driver.find_elements_by_css_selector("input[id='work_position_input']")
for one in mess2:
    one.click()
    time.sleep(1)
mess3 = driver.find_element_by_css_selector("#work_position_click_center_right_list_000000 .on").click()
hz = driver.find_element_by_css_selector("#work_position_click_center_right_list_category_000000_080200").click()
sure = driver.find_element_by_css_selector("#work_position_click_bottom_save").click()
search = driver.find_element_by_css_selector(".ush button").click()

jobs = driver.find_elements_by_css_selector("#resultList div[class='el']")
for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    stringFilelds = [field.text for field in fields]
    print(' | '.join(stringFilelds))

driver.quit()