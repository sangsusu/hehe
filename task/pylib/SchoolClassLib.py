import requests
from cfg import g_vcode
from pprint import pprint

class SchoolClassLib:

    URL = 'http://ci.ytesting.com/api/3school/school_classes'


    def list_school_class(self,gradeid=None):

        if gradeid !=None:
            params = {
                'vcode':g_vcode,
                'action':'list_classes_by_schoolgrade',
                'gradeid':int(gradeid)
            }
        else:
            params = {
                'vcode': g_vcode,
                'action': 'list_classes_by_schoolgrade'
            }

        response = requests.get(self.URL,params=params)

        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict


    def add_school_class(self,gradeid,name,studentlimit):

        payload = {
            'vcode':g_vcode,
            'action':'add',
            'grade':int(gradeid),
            'name':name,
            'studentlimit':int(studentlimit)
        }

        response = requests.post(self.URL,data=payload)

        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict


    def delete_school_class(self,classid):

        payload = {
            'vcode':g_vcode
        }

        url = f'{self.URL}/{classid}'

        response = requests.delete(url,data=payload)

        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict



    def delete_all_school_classes(self):
        #先列出所有班级
        rd = self.list_school_class()
        pprint(rd,indent=2)              #indent=2 缩进两格

        #删除列出的所有班级
        for one in rd['retlist']:          #根据接口文档可知，班级信息都在列出课程接口响应中的retlist中
            self.delete_school_class(one['id'])

        #再列出所有班级
        rd = self.list_school_class()
        pprint(rd,indent=2)

        #若没有删除干净，通过异常报错给rf
        if rd['retlist'] != []:
            raise Exception("cannot delete all school classes!")




    def classlist_should_contain(self,classlist,gradename,classid,invitecode,classname,studentlimit,studentnumber,expectedtimes=1):

        item = {
            "grade__name": gradename,
            "id": classid,
            "invitecode": invitecode,
            "name": classname,
            "studentlimit": int(studentlimit),
            "studentnumber": int(studentnumber),
            "teacherlist": []
        }

        pprint(item)
        pprint('-------------------------------')
        pprint(classlist)

        occurTimes = classlist.count(item)

        if occurTimes != expectedtimes:
            raise Exception(f'班级列表包含了{occurTimes}次指定信息,期望包含{expectedtimes}次!')



    def modify_school_class(self,classid,name,studentlimit):

        payload = {
            'vcode': g_vcode,
            'action': 'modify',
            'name': name,
            'studentlimit': int(studentlimit)
        }

        url = f'{self.URL}/{classid}'     #还可写作 url = '{}/{}'.format(self.URL,classid)

        response = requests.put(url, data=payload)

        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict




