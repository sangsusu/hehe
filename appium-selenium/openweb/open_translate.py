from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
ele = driver.find_element_by_id("kw")
ele.send_keys("翻译")
ele.button = driver.find_element_by_id("su")
ele.button.click()

time.sleep(2)

ele = driver.find_element_by_css_selector("textarea[name='query']")
ele.send_keys("工作年限")
ele = driver.find_element_by_css_selector("a[href=\'#'][class='c-btn c-btn-primary op_translation_btn  OP_LOG_BTN']")
ele.click()

time.sleep(2)

# ele = driver.find_element_by_css_selector("div[class='output-bd'][dir='ltr']")
# print(ele.text)