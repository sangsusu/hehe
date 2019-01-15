from pylib.SchoolClassLib import SchoolClassLib
sc = SchoolClassLib()



class c000003:

    def steps(self):
        print('''\n\n***** step 1 ****  添加 7年级1班 \n''')
        self.ret1 = sc.add_school_class(1, '1班', 60)
        if self.ret1['retcode'] != 1:
            raise Exception('返回值非1')

        if self.ret1['reason'] != 'duplicated class name':
            raise Exception('错误吗不对')


        print('''\n\n***** step 2 ****  列出班级，检验一下\n''')

        ret = sc.list_school_class(1)
        sc.classlist_should_not_contain(ret['retlist'],
                                    '1班',
                                    '七年级',
                                    self.ret1['invitecode'],
                                    60,
                                    0,
                                    self.ret1['id'])


    def setup(self):
        pass

    def teardown(self):
        pass
