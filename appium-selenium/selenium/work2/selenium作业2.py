from selenium import webdriver

driver = webdriver.Chrome()
# driver.implicitly_wait(1)
driver.get("http://music.baidu.com/top/new")


songInfo = driver.find_elements_by_css_selector('.song-item')
for one in songInfo:
    upsign = one.find_elements_by_css_selector('.up')
    if upsign:
        name = one.find_element_by_css_selector("span>a[href^='/song']").text
        author = one.find_element_by_css_selector("span [class='author_list']").text
        print(f'{name:10}:{author}')

driver.quit()

