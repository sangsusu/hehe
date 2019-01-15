from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://tinypng.com/')

driver.find_element_by_css_selector('section .target .icon').click()
time.sleep(1)

import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")
shell.Sendkeys(r"e:\123"+'\n')

time.sleep(5)
driver.quit()
