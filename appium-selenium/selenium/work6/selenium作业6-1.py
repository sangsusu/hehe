from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.vmall.com/')

driver.find_element_by_css_selector(".shortcut div ul li a[href='http://consumer.huawei.com/cn/']").click()

mainwindow = driver.current_window_handle

for handle in driver.window_handles:
    driver.switch_to_window(handle)
    if '华为消费者业务' in driver.title:
        break

titles = driver.find_elements_by_css_selector("#top_nav .menu li a[class='a-common']")
titlelist = []
for one in titles:
    titlelist.append(one.text)
if titlelist == ['智能手机','笔记本&平板','穿戴设备','智能家居','更多产品','软件应用','服务与支持','华为商城']:
    print('华为官网主菜单显示正确')
else:
    print('华为官网主菜单显示错误')

driver.switch_to_window(mainwindow)

driver.find_element_by_css_selector('.s-sub li:nth-last-child(1) a').click()

driver.find_element_by_css_selector("a[href='http://appstore.huawei.com/']").click()

for handle in driver.window_handles:
    driver.switch_to_window(handle)
    if '华为应用市场' in driver.title:
        break

Thetitles = driver.find_elements_by_css_selector('.ul-nav>li a')
t2list = []
for one in Thetitles:
    t2list.append(one.text)
if t2list == ['首页','游戏','软件','专题','品牌专区','华为软件专区']:
    print('应用市场主菜单显示正确')
else:
    print('应用市场主菜单显示错误')

driver.switch_to_window(mainwindow)

from selenium.webdriver.common.action_chains import ActionChains
ac = ActionChains(driver)
ac.move_to_element(driver.find_element_by_css_selector('#zxnav_1')).perform()

eles = driver.find_elements_by_css_selector('#zxnav_1 > div.category-panels > ul a ')

eletext = [ele.text for ele in eles]
expectlist = ['平板电脑','笔记本电脑','笔记本配件']
if eletext == expectlist:
    print('显示的菜单有平板电脑  笔记本电脑 笔记本配件')
else:
    print('显示的菜单有误')

driver.quit()

