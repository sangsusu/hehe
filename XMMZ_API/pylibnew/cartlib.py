import requests, json
from cfgnew import *
from pprint import pprint
from robot.api import logger

class  cartlib:
    URL = "https://a.lrlz.com/mobile/index.php"

    def __init__(self):
        self.sessid = sessid

    def set_sessid(self, sessid):
        self.sessid = sessid


    def login(self,mobile,code):
        params = {
            'act': 'login',
            'op': 'bind_mobilex',
            'mobile': mobile,
            'code': code,
            'client_type':'ios',
        }

        response = requests.get(self.URL, params=params,verify=False)
        bodyDict = response.json()
        pprint(bodyDict, indent=2)
        return bodyDict



    # def list_cart_goods(self):
    #     p = {
    #         'sessid': self.sessid,
    #         'act': 'cart',
    #         'op': 'list',
    #         'page': '20',
    #         'from': 'b3A9bGlzdCZtaW5lc3RfY2FydGlkPTAmYWN0PWNhcnQmcGFnZT0yMA%3D%3D',
    #         'minest_cartid': 0
    #     }
    #     header = {
    #         'sessid': self.sessid
    #     }
    #     response = requests.get(self.URL, params=p, verify=False)
    #
    #     bodyDict = response
    #     pprint (bodyDict,indent=2)
    #     return bodyDict



    # def delete_school_class(self,classid):
    #     payload = {
    #         'sessid'  : self.sessid,
    #     }
    #
    #     url = '{}/{}'.format(self.URL,classid)
    #     response = requests.delete(url,data=payload)
    #
    #     return response.json()




    # def add_school_class(self,gradeid,name,studentlimit):
    #     payload = {
    #         'vcode'  : self.vcode,
    #         'action' : 'add',
    #         'grade'  : int(gradeid),
    #         'name'   : name,
    #         'studentlimit'  : int(studentlimit),
    #     }
    #     response = requests.post(self.URL,data=payload)
    #
    #     bodyDict = response.json()
    #     pprint (bodyDict,indent=2)
    #     # logger.debug('ret：\n{}'.format(json.dumps(bodyDict, indent=1)))
    #
    #     return bodyDict


    # def delete_all_school_classes(self):
    #     # 先列出所有班级
    #     rd =  self.list_school_class()
    #     pprint(rd, indent=2)
    #
    #     # 删除列出的所有班级
    #     for one in rd['retlist']:
    #         self.delete_school_class(one['id'])
    #
    #     #再列出七年级所有班级
    #     rd =  self.list_school_class(1)
    #     pprint (rd,indent=2)
    #
    #     # 如果没有删除干净，通过异常报错给RF
    #     # 参考http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#reporting-keyword-status
    #     if rd['retlist'] != []:
    #         raise  Exception("cannot delete all school classes!!")


    # def classlist_should_contain(self,
    #                              classlist,
    #                              classname,
    #                              gradename,
    #                              invitecode,
    #                              studentlimit,
    #                              studentnumber,
    #                              classid,
    #                             expectedtimes=1
    #                                 ):
    #
    #     item = {
    #         "name": classname,
    #         "grade__name": gradename,
    #         "invitecode": invitecode,
    #         "studentlimit": int(studentlimit),
    #         "studentnumber": int(studentnumber),
    #         "id": classid,
    #         "teacherlist": []
    #     }
    #
    #     occurTimes = classlist.count(item)
    #     logger.info('occur {} times'.format(occurTimes))
    #
    #     if occurTimes != expectedtimes:
    #         # 通过抛出异常来让关键字Fail
    #
    #         raise Exception(
    #             'class list contain your class info {} times,expect {} times!!'.format(
    #                 occurTimes, expectedtimes)
    #         )



    # def classlist_should_not_contain(self,
    #                              classlist,
    #                              classname,
    #                              gradename,
    #                              invitecode,
    #                              studentlimit,
    #                              studentnumber,
    #                              classid
    #                                 ):
    #
    #     item = {
    #         "name": classname,
    #         "grade__name": gradename,
    #         "invitecode": invitecode,
    #         "studentlimit": int(studentlimit),
    #         "studentnumber": int(studentnumber),
    #         "id": classid,
    #         "teacherlist": []
    #     }
    #
    #     occurTimes = classlist.count(item)
    #     logger.info('occur {} times'.format(occurTimes))
    #
    #     if occurTimes > 0:
    #         # 通过抛出异常来让关键字Fail
    #
    #         raise Exception('班级包含了指定班级信息')


# if __name__ == '__main__':
#     scm = SchoolClassLib()
#     ret = scm.list_school_class(1)

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

