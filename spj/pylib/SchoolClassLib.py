import requests,json
from cfg import g_vcode
from pprint import pprint
from robot.api import logger

class  SchoolClassLib:
    URL = "http://ci.ytesting.com/api/3school/school_classes"

    def __init__(self):
        self.vcode = g_vcode

    def set_vcode(self,vcode):
        self.vcode = vcode


    def delete_school_class(self,classid):
        payload = {
            'vcode'  : self.vcode,
        }

        url = '{}/{}'.format(self.URL,classid)
        response = requests.delete(url,data=payload)

        return response.json()


    def list_school_class(self,gradeid=None):
        if gradeid != None:
            params = {
                'vcode':self.vcode,
                'action':'list_classes_by_schoolgrade',
                'gradeid':int(gradeid)
            }
        else:
            params = {
                'vcode':self.vcode,
                'action':'list_classes_by_schoolgrade'
            }

        response = requests.get(self.URL,params=params)

        bodyDict = response.json()
        pprint (bodyDict,indent=2)
        return bodyDict


    def add_school_class(self,gradeid,name,studentlimit):
        payload = {
            'vcode'  : self.vcode,
            'action' : 'add',
            'grade'  : int(gradeid),
            'name'   : name,
            'studentlimit'  : int(studentlimit),
        }
        response = requests.post(self.URL,data=payload)

        bodyDict = response.json()
        pprint (bodyDict,indent=2)
        # logger.debug('ret：\n{}'.format(json.dumps(bodyDict, indent=1)))

        return bodyDict


    def delete_all_school_classes(self):
        # 先列出所有班级
        rd =  self.list_school_class()
        pprint(rd, indent=2)

        # 删除列出的所有班级
        for one in rd['retlist']:
            self.delete_school_class(one['id'])

        #再列出七年级所有班级
        rd =  self.list_school_class(1)
        pprint (rd,indent=2)

        # 如果没有删除干净，通过异常报错给RF
        # 参考http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#reporting-keyword-status
        if rd['retlist'] != []:
            raise  Exception("cannot delete all school classes!!")

    def classlist_should_contain(self,
                                 classlist,
                                 classname,
                                 gradename,
                                 invitecode,
                                 studentlimit,
                                 studentnumber,
                                 classid,
                                expectedtimes=1
                                    ):

        item = {
            "name": classname,
            "grade__name": gradename,
            "invitecode": invitecode,
            "studentlimit": int(studentlimit),
            "studentnumber": int(studentnumber),
            "id": classid,
            "teacherlist": []
        }

        occurTimes = classlist.count(item)
        logger.info('occur {} times'.format(occurTimes))

        if occurTimes != expectedtimes:
            # 通过抛出异常来让关键字Fail

            raise Exception(
                'class list contain your class info {} times,expect {} times!!'.format(
                    occurTimes, expectedtimes)
            )



    def classlist_should_not_contain(self,
                                 classlist,
                                 classname,
                                 gradename,
                                 invitecode,
                                 studentlimit,
                                 studentnumber,
                                 classid
                                    ):

        item = {
            "name": classname,
            "grade__name": gradename,
            "invitecode": invitecode,
            "studentlimit": int(studentlimit),
            "studentnumber": int(studentnumber),
            "id": classid,
            "teacherlist": []
        }

        occurTimes = classlist.count(item)
        logger.info('occur {} times'.format(occurTimes))

        if occurTimes > 0:
            # 通过抛出异常来让关键字Fail

            raise Exception('班级包含了指定班级信息')


if __name__ == '__main__':
    scm = SchoolClassLib()
    ret = scm.list_school_class(1)

    # ret = scm.add_school_class(1,'新测试',77)
    # print(json.dumps(ret, indent=2))
    #
    # ret = scm.delete_school_class(28)
    # print(json.dumps(ret, indent=2))
    #
    # ret = scm.list_school_class(1)
    # print(json.dumps(ret, indent=2))
    # #
    # scm.delete_all_school_classes()

