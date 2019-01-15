from  selenium  import  webdriver
from Var import *
from selenium.webdriver.support.ui import Select
import time

class WebOpAdmin():
    #保证仅实例化一次
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def SetupWebtest(self,driverType='chrome'):
        #self.cur_wd保存webdriver对象
        self.cur_wd = None
        if driverType == 'chrome':
            self.cur_wd = webdriver.Chrome()
        elif driverType == 'firefox':
            self.cur_wd = webdriver.Firefox()
        else:
            raise Exception('unknow driver type %s' % driverType)

        self.cur_wd.implicitly_wait(3)


    def TeardownWebtest(self):
        self.cur_wd.quit()


    def adminloginWebsite(self):
        self.cur_wd.get(MgrLoginUrl)
        self.cur_wd.find_element_by_id('username').send_keys(adminuser['name'])
        self.cur_wd.find_element_by_id('password').send_keys(adminuser['pw'])
        self.cur_wd.find_element_by_tag_name('button').click()


    def add_course(self,name,desc,idx):
        self.cur_wd.find_element_by_css_selector("ul.nav a[href='#/']").click()
        time.sleep(1)

        self.cur_wd.find_element_by_css_selector("button[ng-click='showAddOne=true']").click()

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addData.name']")
        ele.clear()  #文本输入要先做清除
        ele.send_keys(name)

        ele = self.cur_wd.find_element_by_tag_name("textarea")
        ele.clear()
        ele.send_keys(desc)

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        self.cur_wd.find_element_by_css_selector("button[ng-click='addOne()']").click()

        time.sleep(1)


    def add_teacher(self,realname,username,desc,idx,course):
        self.cur_wd.find_element_by_css_selector("ul.nav a[href='#/teacher']").click()
        time.sleep(1)

        self.cur_wd.find_element_by_css_selector("button[ng-click^=showAddOne]").click()
        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addEditData.realname']")
        ele.clear()  #文本输入要先做清除
        ele.send_keys(realname)

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addEditData.username']")
        ele.clear()
        ele.send_keys(username)

        ele = self.cur_wd.find_element_by_css_selector("textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(desc)

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addEditData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        select = Select(self.cur_wd.find_element_by_css_selector("select[ng-model='$parent.courseSelected']"))
        select.select_by_visible_text(course)

        self.cur_wd.find_element_by_css_selector("button[ng-click='addEditData.addTeachCourse()']").click()
        self.cur_wd.find_element_by_css_selector("button[ng-click='addOne()']").click()
        time.sleep(1)




    def deleteAllCourse(self):
        self.cur_wd.find_element_by_css_selector("ul.nav a[href='#/']").click()
        time.sleep(1)

        self.cur_wd.implicitly_wait(1)
        while True:
            delbuttons = self.cur_wd.find_elements_by_css_selector("button[ng-click='delOne(one)']")
            if delbuttons == []:
                break
            delbuttons[0].click()
            self.cur_wd.find_element_by_css_selector('button.btn-primary').click()
            time.sleep(1)
        self.cur_wd.implicitly_wait(3)



    def deleteAllTeacher(self):
        self.cur_wd.find_element_by_css_selector("ul.nav a[href='#/teacher']").click()
        time.sleep(1)
        self.cur_wd.implicitly_wait(1)
        while True:
            delbuttons = self.cur_wd.find_elements_by_css_selector("button[ng-click='delOne(one)']")
            if delbuttons == []:
                break
            delbuttons[0].click()
            self.cur_wd.find_element_by_css_selector("button[class='btn btn-primary']").click()
            time.sleep(1)

        self.cur_wd.implicitly_wait(3)




    def getcourselist(self):
        self.cur_wd.find_element_by_css_selector("ul.nav a[href='#/']").click()
        time.sleep(1)
        eles = self.cur_wd.find_elements_by_css_selector("tr>td:nth-child(2)")
        return [ele.text for ele in eles]




    def getteacherlist(self):
        self.cur_wd.find_element_by_css_selector("ul.nav a[href='#/teacher']").click()
        time.sleep(1)
        eles = self.cur_wd.find_elements_by_css_selector("tr>td:nth-child(2)")
        return [ele.text for ele in eles]



    def deleteAllTrainCourse(self):
        self.cur_wd.find_element_by_css_selector("ul.nav a[ href='#/training']").click()
        time.sleep(1)

        self.cur_wd.implicitly_wait(1)
        while True:
            delbuttons = self.cur_wd.find_elements_by_css_selector("button[ng-click='delOne(one)']")
            if delbuttons == []:
                break
            delbuttons[0].click()
            self.cur_wd.find_element_by_css_selector('button.btn-primary').click()
            time.sleep(1)

        self.cur_wd.implicitly_wait(3)




    def deleteAllTrainSchedule(self):
        self.cur_wd.find_element_by_css_selector("ul.nav a[ href='#/traininggrade']").click()
        time.sleep(1)

        self.cur_wd.implicitly_wait(1)
        while True:
            delbuttons = self.cur_wd.find_elements_by_css_selector("button[ng-click='delOne(one)']")
            if delbuttons == []:
                break
            delbuttons[0].click()
            self.cur_wd.find_element_by_css_selector('button.btn-primary').click()
            time.sleep(1)

        self.cur_wd.implicitly_wait(3)





    def addTrainCourse(self,classname,desc,idx,course1,course2):
        self.cur_wd.find_element_by_css_selector("ul.nav a[ href='#/training']").click()
        self.cur_wd.find_element_by_css_selector("button[ng-click='showAddOne=true']").click()

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addEditData.name']")
        ele.clear()
        ele.send_keys(classname)

        ele = self.cur_wd.find_element_by_css_selector("textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(desc)

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addEditData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        select = Select(self.cur_wd.find_element_by_css_selector("select[ng-model='$parent.courseSelected']"))
        select.select_by_visible_text(course1)

        self.cur_wd.find_element_by_css_selector("button[ng-click='addEditData.addTeachCourse()']").click()

        select = Select(self.cur_wd.find_element_by_css_selector("select[ng-model='$parent.courseSelected']"))
        select.select_by_visible_text(course2)

        self.cur_wd.find_element_by_css_selector("button[ng-click='addEditData.addTeachCourse()']").click()


        self.cur_wd.find_element_by_css_selector("button[ng-click='addOne()']").click()





    def addTrainSchedule(self,schedule,desc,idx,course):
        self.cur_wd.find_element_by_css_selector("ul.nav a[ href='#/traininggrade']").click()
        self.cur_wd.find_element_by_css_selector("button[ng-click='showAddOne=true']").click()

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addEditData.name']")
        ele.clear()
        ele.send_keys(schedule)

        ele = self.cur_wd.find_element_by_css_selector("textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(desc)

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addEditData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        select = Select(self.cur_wd.find_element_by_css_selector("select[ng-model='$parent.addEditData.training_id']"))
        select.select_by_visible_text(course)

        self.cur_wd.find_element_by_css_selector("button[ng-click='addOne()']").click()





    def getTrainCourselist(self):
        self.cur_wd.find_element_by_css_selector("ul.nav a[ href='#/training']").click()
        time.sleep(1)
        eles = self.cur_wd.find_elements_by_css_selector("tr>td:nth-child(2)")
        return [ele.text for ele in eles]




    def getSchedulelist(self):
        self.cur_wd.find_element_by_css_selector("ul.nav a[ href='#/traininggrade']").click()
        time.sleep(1)
        eles = self.cur_wd.find_elements_by_css_selector("tr>td:nth-child(2)")
        return [ele.text for ele in eles]


    def deletStudent(self):
        self.cur_wd.find_element_by_css_selector("ul.nav a[href='#/student']").click()
        time.sleep(1)

        self.cur_wd.implicitly_wait(1)
        while True:
            delbuttons = self.cur_wd.find_elements_by_css_selector("button[ng-click='delOne(one)']")
            if delbuttons == []:
                break
            delbuttons[0].click()
            self.cur_wd.find_element_by_css_selector('button.btn-primary').click()
            time.sleep(1)

        self.cur_wd.implicitly_wait(3)



    def getStudentlist(self):
        self.cur_wd.find_element_by_css_selector("ul.nav a[ href='#/student']").click()
        time.sleep(1)
        eles = self.cur_wd.find_elements_by_css_selector("tr>td:nth-child(1)")
        return [ele.text for ele in eles]





    def addStudent(self,sname,lname,desc,course,schedule):
        self.cur_wd.find_element_by_css_selector("ul.nav a[ href='#/student']").click()
        self.cur_wd.find_element_by_css_selector("button[ng-click='showAddOne=true']").click()

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addEditData.realname']")
        ele.clear()
        ele.send_keys(sname)

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addEditData.username']")
        ele.clear()
        ele.send_keys(lname)

        ele = self.cur_wd.find_element_by_css_selector("textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(desc)

        select = Select(self.cur_wd.find_element_by_css_selector("select[ng-model='$parent.addEditData.training_id']"))
        select.select_by_visible_text(course)

        select = Select(self.cur_wd.find_element_by_css_selector("select[ng-model='$parent.addEditData.traininggrade_id']"))
        select.select_by_visible_text(schedule)

        self.cur_wd.find_element_by_css_selector("button[ng-click='addOne()']").click()