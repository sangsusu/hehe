from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com/?tn=99502248_hao_pg')
driver.find_element_by_css_selector("#u1 a[href='http://news.baidu.com']").click()
driver.find_element_by_id('channel-shanghai')
driver.find_element_by_css_selector('#pane-news .hdline0 a').click()

mainwindow = driver.current_window_handle

for handle in driver.window_handles:
    driver.switch_to_window(handle)
    if '习近平' in driver.title:
        break

article = driver.find_element_by_class_name('text_c')
print(article.text)

driver.close()