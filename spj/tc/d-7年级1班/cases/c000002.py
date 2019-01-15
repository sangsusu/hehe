from pylib.SchoolClassLib import SchoolClassLib
sc = SchoolClassLib()

class c000002:

    def steps(self):
        print('''\n\n***** step 1 ****  添加 7年级2班 \n''')
        self.ret1 = sc.add_school_class(1, '2班', 60)
        if self.ret1['retcode'] != 0:
            raise Exception('返回值非0')



        print('''\n\n***** step 2 ****  列出班级，检验一下\n''')

        ret = sc.list_school_class(1)
        sc.classlist_should_contain(ret['retlist'],
                                    '2班',
                                    '七年级',
                                    self.ret1['invitecode'],
                                    60,
                                    0,
                                    self.ret1['id'])


    def setup(self):
        pass

    def teardown(self):
        sc.delete_school_class(self.ret1['id'])
