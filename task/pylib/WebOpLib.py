from selenium import webdriver
import time,pprint
from cfg import *
from selenium.webdriver.common.action_chains import ActionChains

class WebOpLib():

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'   # 保证仅实例化一次

    def open_browser(self):   # 打开浏览器
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)


    def close_browser(self):   # 关闭浏览器
        self.wd.quit()



    def teacher_login(self, username, password):
        self.wd.get(g_teacher_login_url)

        self.wd.find_element_by_id('username').send_keys(username)
        self.wd.find_element_by_id('password').send_keys(password)
        self.wd.find_element_by_id('submit').click()

        self.wd.find_element_by_id('home_div')



    def get_teacher_homepage_info(self):

        self.wd.find_element_by_css_selector("a[href='#/home']>li").click()  # 点击主页

        time.sleep(2)   # 稍等一下，防止数据还没展示出来

        # 取出需要的六个元素的值，这里利用了前端框架Angular的特征，数据绑在ng-binding上
        eles = self.wd.find_elements_by_css_selector('#page-wrapper .ng-binding')

        homepage_info = [ele.text for ele in eles]

        pprint.pprint(homepage_info)
        return homepage_info



    def get_teacher_class_students_info(self):

        ele = self.wd.find_elements_by_css_selector("li[style='cursor: pointer;']")[-2]    # 班级情况的元素定位

        ac = ActionChains(self.wd)
        ac.move_to_element(ele).perform()    # 模拟鼠标停留在该元素

        ele = self.wd.find_element_by_css_selector("a[href='#/student_group']>li span")     # 点击 班级学生
        ele.click()

        time.sleep(2)

        classStudentTable = {}

        classes = self.wd.find_elements_by_css_selector("div.panel-green")   # 所有班级

        for cla in classes:
            gradeclass = cla.find_element_by_css_selector(".panel-heading")
            title = gradeclass.text.replace(' ', '')

            gradeclass.click()
            time.sleep(2)

            self.wd.implicitly_wait(3)
            studenteles = cla.find_elements_by_css_selector('tr>td:nth-child(2)')    # 班级表中的学生姓名
            self.wd.implicitly_wait(10)

            names = [ele.text for ele in studenteles]

            classStudentTable[title] = names

        pprint.pprint(classStudentTable)

        return classStudentTable



# if __name__ == '__main__':
#     webop = WebOpLib()
#     webop.open_browser()
#     webop.teacher_login(teacher['username'], teacher['password'])
#
#     webop.get_teacher_class_students_info()
#
#     webop.get_teacher_homepage_info()
#
#     webop.close_browser()




    def student_login(self, username, password):
        self.wd.get(g_student_login_url)

        self.wd.find_element_by_id('username').send_keys(username)
        self.wd.find_element_by_id('password').send_keys(password)
        self.wd.find_element_by_id('submit').click()

        self.wd.find_element_by_id('div-home')



    def get_student_homepage_info(self):

        self.wd.find_element_by_css_selector("a[href='#/home']>li").click()  # 点击主页

        time.sleep(2)   # 稍等一下，防止数据还没展示出来

        # 取出需要的元素的值，这里利用了前端框架Angular的特征，数据绑在ng-binding上
        eles = self.wd.find_elements_by_css_selector('#page-wrapper .ng-binding')

        homepage_info = [ele.text for ele in eles]

        new_homepage_info = [homepage_info[0], homepage_info[1], homepage_info[3], homepage_info[4]]

        pprint.pprint(new_homepage_info)
        return new_homepage_info



    def student_error_bank(self):

        self.wd.find_element_by_css_selector("a[href='#/yj_wrong_questions']>li").click()  # 点击错题库

        time.sleep(2)   # 稍等一下，防止数据还没展示出来

        ele = self.wd.find_element_by_css_selector(".col-lg-12 span")

        bank_info = ele.text

        pprint.pprint(bank_info)
        return bank_info


# if __name__ == '__main__':
#     webop = WebOpLib()
#     webop.open_browser()
#     webop.student_login('sangsang1','888888')
#
#     webop.get_student_homepage_info()
#
#     webop.student_error_bank()
#
#     webop.close_browser()



    def teacher_create_task(self, exam_name):

        self.wd.find_elements_by_id('members')[1].click()   # 点击作业

        self.wd.find_element_by_css_selector("[ng-click='show_page_addexam()']>li").click()   # 点击创建作业

        time.sleep(1)

        self.wd.find_element_by_id('exam_name_text').send_keys(exam_name)    # 输入作业名称
        time.sleep(1)
        self.wd.find_element_by_id('btn_pick_question').click()         # 点击从题库选择题目

        time.sleep(3)

        # 题目在新的frame中
        self.wd.switch_to_frame('pick_questions_frame')

        self.wd.find_element_by_id('ZJ_1_anchor')

        # 只需选前3个，每次选择1题，界面会重新渲染，所以只能循环获取

        for counter in range(3):
            selectButtons = self.wd.find_elements_by_class_name('btn_pick_question')
            selectButtons[counter].click()
            # 点击后界面重新渲染，等待一下
            time.sleep(1)

        # self.wd.find_element_by_id('ZJ_1_0_0').click()   # 点击第一章第一节 从自然数到有理数
        # time.sleep(2)
        # choice_question_area = self.wd.find_element_by_css_selector("div[style='margin-right:20px; min-width:550px;max-width:800px;']")
        #  右边的选择题区域

        # userful_buttons = choice_question_area.find_elements_by_css_selector("div[data-toggle='buttons'] label:nth-child(2)")
        # # 所有的 加入试题篮按钮
        # for one in userful_buttons[:3]:
        #     one.click()
        #     time.sleep(1)

        self.wd.find_element_by_css_selector('#cart_footer .btn-group .btn-blue').click()  # 点击确定

        # 切换回 主 html
        self.wd.switch_to.default_content()

        # 选完题目回到主界面，界面会发生变动，sleep一下
        time.sleep(1)

        self.wd.find_element_by_id('btn_submit').click()   # 点击确定添加
        time.sleep(1)

        self.wd.find_elements_by_css_selector('.bootstrap-dialog-footer-buttons button')[-1].click()
        # 点击 发布给学生

        time.sleep(2)

        # 切换到 下发学习任务窗口

        # 保存主窗口handle
        mainWindow = self.wd.current_window_handle

        for handle in self.wd.window_handles:
            # 切换到新窗口
            self.wd.switch_to_window(handle)
            # 检查是否是我们要进入的window
            if '下发学习任务' in self.wd.title:
                print('进入到下发任务窗口')
                break
        time.sleep(1)

        self.wd.find_element_by_css_selector("input[ng-model='student.checked']+span").click()
        # 勾选学生

        self.wd.find_element_by_css_selector("button[ng-click='openDispatchDlg()']").click()
        # 点击 确定下发

        time.sleep(2)

        self.wd.find_element_by_css_selector("button[ng-click='dispatchIt()']").click()
        # 点击 确定 下发给该学生
        time.sleep(1)

        self.wd.find_element_by_css_selector("button[class='btn btn-default']").click()
        # 点击 确定 提示已发布

        # 切换回主窗口
        self.wd.switch_to_window(mainWindow)

# if __name__ == '__main__':
#     webop = WebOpLib()
#     webop.open_browser()
#     webop.teacher_login(teacher['username'], teacher['password'])
#
#     webop.create_task()




    def student_do_exam(self):
        self.wd.find_element_by_css_selector(".main-menu [href='#/task_manage']>li").click()    # 点击 我的任务

        # 由于数据是异步获取，需要sleep一段时间，假设需求是2秒必须获取数据
        time.sleep(2)
        self.wd.find_element_by_css_selector("table [ng-click='viewTask(taskTrack)']").click()  # 点击打开第一个任务

        sellection = self.wd.find_elements_by_css_selector(".btn-group button:nth-child(2)")   # 选择3个B
        for one in sellection:
            one.click()
            time.sleep(1)

        self.wd.find_element_by_css_selector("button[ng-click='saveMyResult(true)']").click()  # 点击提交
        time.sleep(1)

        self.wd.find_element_by_css_selector(".bootstrap-dialog-footer-buttons .btn-primary").click()  # 点击确定
        time.sleep(1)


# if __name__ == '__main__':
#     webop = WebOpLib()
#     webop.open_browser()
#     webop.student_login('sangsang1','888888')
#
#     webop.studentDoExam()



    def teacher_check_exam(self):

        self.wd.find_elements_by_id('members')[1].click()    # 点击作业

        self.wd.find_element_by_css_selector("a[href='#/task_manage?tt=1'] .submenu-title").click()    # 点击已发布作业

        time.sleep(1)

        self.wd.find_element_by_css_selector("a[ng-click='trackTask(task)']").click()   # 点击第一个作业的完成情况
        time.sleep(1)

        self.wd.find_element_by_css_selector("button[ng-click*='viewTaskTrack']").click()    # 点击 查看

        # 保存主窗口handle
        mainWindow = self.wd.current_window_handle

        for handle in self.wd.window_handles:
            # 切换到新窗口
            self.wd.switch_to_window(handle)
            # 检查是否是我们要进入的window
            if '查看作业' in self.wd.title:
                print('进入到查看作业窗口')
                break
        time.sleep(1)

        # 勾选的选项会有.myCheckbox input:checked 风格修饰
        # 但是这个不出现在 元素html里面

        eles = self.wd.find_elements_by_css_selector('.myCheckbox input:checked')

        selectedchoices = [ele.find_element_by_xpath('./..').text.strip() for ele in eles]    # 选项abcd在其父元素label里

        print(selectedchoices)


        # 切回主窗口
        self.wd.switch_to_window(mainWindow)

        return selectedchoices


# if __name__ == '__main__':
#     webop = WebOpLib()
#     webop.open_browser()
#
#     webop.teacher_login('sangsang', '888888')
#     webop.teacher_create_task('test003')
#
#     webop.student_login('sangsang1', '888888')
#     webop.student_do_exam()
#
#     webop.teacher_login('sangsang', '888888')
#     webop.teacher_check_exam()
















