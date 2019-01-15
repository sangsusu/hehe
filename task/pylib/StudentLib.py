import requests,json
from cfg import g_vcode
from pprint import pprint
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn


class StudentLib:

    URL = 'http://ci.ytesting.com/api/3school/students'

    def __init__(self):
        self.vcode = g_vcode

    def set_vcode(self,vcode):
        self.vcode = vcode         # 用来改vcode的，如果要验证错误的vcode的话


    def list_student(self):
        params = {
            'vcode': self.vcode,
            'action': 'search_with_pagenation'
        }

        response = requests.get(self.URL,params=params)

        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict


    def add_student(self,username,realname,gradeid,classid,phonenumber,idSavedname=None):

        payload = {
            'vcode': self.vcode,
            'action': 'add',
            'username': username,
            'realname': realname,
            'gradeid': gradeid,
            'classid': classid,
            'phonenumber': phonenumber
        }

        response = requests.post(self.URL, data=payload)

        bodyDict = response.json()
        pprint(bodyDict)

        if idSavedname:
            print('before')
            BuiltIn().set_global_variable('${%s}'%idSavedname,bodyDict['id'])
            print(f"global var set: ${idSavedname}:{bodyDict['id']}")

        return bodyDict


    def delete_student(self,studentid):

        payload = {
            'vcode':self.vcode
        }

        url = f'{self.URL}/{studentid}'

        response = requests.delete(url, data=payload)

        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict


    def delete_all_students(self):
        # 先列出所有学生
        rd = self.list_student()

        # 删除列出的所有学生
        for one in rd['retlist']:             # 根据接口文档可知，信息都在列出学生接口响应中的retlist中
            self.delete_student(one['id'])

        # 再列出所有学生
        rd = self.list_student()

        # 若没有删除干净，通过异常报错给rf
        if rd['retlist']:
            raise Exception("cannot delete all school classes!")


    def studentlist_should_contain(self,
                                   studentlist,
                                   username,
                                   realname,
                                   studentid,
                                   phonenumber,
                                   classid,
                                   expectedtimes=1):

        item = {
            "username": username,
            "realname": realname,
            "id": int(studentid),
            "phonenumber": phonenumber,
            "classid": int(classid)
        }

        occurTimes = studentlist.count(item)
        logger.info('occur {} times'.format(occurTimes))

        if occurTimes != int(expectedtimes):
            raise Exception(f'学生列表包含了{occurTimes}次指定信息,期望包含{expectedtimes}次!')


    def modify_student(self,studentid,realname=None,phonenumber=None):

        payload = {
            'vcode': self.vcode,
            'action': 'modify'
        }

        if realname is not None:
            payload['realname'] = realname
        if phonenumber is not None:
            payload['phonenumber'] = phonenumber

        url = f'{self.URL}/{studentid}'     # 还可写作 url = '{}/{}'.format(self.URL,classid)

        response = requests.put(url, data=payload)

        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict



    #if __name__ == '__main__':
    #     scm = studentLib()
    #     ret = scm.list_student(1)



