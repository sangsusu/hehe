import requests,json
from cfg import g_vcode
from pprint import pprint
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

class TeacherLib:

    URL = 'http://ci.ytesting.com/api/3school/teachers'

    def __init__(self):
        self.vcode = g_vcode

    def set_vcode(self,vcode):
        self.vcode = vcode         # 用来改vcode的，如果要验证错误的vcode的话


    def list_teacher(self,subjectid=None):
        params = {
            'vcode': self.vcode,
            'action': 'search_with_pagenation'
        }
        if subjectid !=None:
            params['subjectid'] = subjectid

        response = requests.get(self.URL,params=params)

        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict


    def add_teacher(self,username,realname,subjectid,classlist,phonenumber,email,idcardnumber,idSavedname=None):

        # 230,231,232
        tmpList = str(classlist).split(',')
        newclassList = [{'id':oneid.strip()} for oneid in tmpList if oneid!='']

        payload = {
            'vcode':self.vcode,
            'action':'add',
            'username': username,
            'realname': realname,
            'subjectid': subjectid,
            'classlist': json.dumps(newclassList),
            'phonenumber': phonenumber,
            'email': email,
            'idcardnumber': idcardnumber,
        }

        response = requests.post(self.URL,data=payload)

        bodyDict = response.json()
        pprint(bodyDict)

        if idSavedname:
            print('before')
            BuiltIn().set_global_variable('${%s}'%idSavedname,bodyDict['id'])
            print(f"global var set: ${idSavedname}:{bodyDict['id']}")

        return bodyDict


    def delete_teacher(self,teacherid):

        payload = {
            'vcode':self.vcode
        }

        url = f'{self.URL}/{teacherid}'

        response = requests.delete(url,data=payload)

        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict



    def delete_all_teachers(self):
        # 先列出所有老师
        rd = self.list_teacher()
        pprint(rd,indent=2)              # indent=2 缩进两格

        # 删除列出的所有老师
        for one in rd['retlist']:          # 根据接口文档可知，班级信息都在列出课程接口响应中的retlist中
            self.delete_teacher(one['id'])

        # 再列出所有老师
        rd = self.list_teacher()

        # 若没有删除干净，通过异常报错给rf
        if rd['retlist'] != []:
            raise Exception("cannot delete all school classes!")




    def teacherlist_should_contain(self,
                                   teacherlist,
                                   username,
                                   realname,
                                   teacherid,
                                   classlist,
                                   phonenumber,
                                   email,
                                   idcardnumber,
                                   expectedtimes=1):

        # 确保是字符串，而不是整数
        teachclasslist = str(classlist)

        item = {
            "username": username,
            "teachclasslist": [int(one.strip()) for one in teachclasslist.split(',') if one.strip()!= ''],
            "realname": realname,
            "id": int(teacherid),
            "phonenumber": phonenumber,
            "email": email,
            "idcardnumber": idcardnumber
        }

        pprint(item)
        pprint('-------------------------------')
        pprint(classlist)

        occurTimes = teacherlist.count(item)
        logger.info('occur {} times'.format(occurTimes))

        if occurTimes != int(expectedtimes):
            raise Exception(f'老师列表包含了{occurTimes}次指定信息,期望包含{expectedtimes}次!')



    def modify_teacher(self,teacherid,realname=None,subjectid=None,classlist=None,phonenumber=None,email=None,idcardnumber=None):

        payload = {
            'vcode': self.vcode,
            'action': 'modify'
        }

        if realname is not None:
            payload['realname'] = realname
        if subjectid is not None:
            payload['subjectid'] = subjectid
        if phonenumber is not None:
            payload['phonenumber'] = phonenumber
        if email is not None:
            payload['email'] = email
        if idcardnumber is not None:
            payload['idcardnumber'] = idcardnumber

        if classlist is not None:
            tmpList = str(classlist).split(',')
            newclasslist = [{'id':int(oneid.strip())} for oneid in tmpList if oneid != '']
            payload['classlist'] = json.dumps(newclasslist)

        url = f'{self.URL}/{teacherid}'     # 还可写作 url = '{}/{}'.format(self.URL,classid)

        response = requests.put(url, data=payload)

        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict



    #  if __name__ == '__main__':
    #     scm = TeacherLib()
    #     ret = scm.list_teacher(1)



