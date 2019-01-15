# 1.程序开始的时候提示用户输入学生年龄信息 格式如下：
# Jack Green ,   21  ;  Mike Mos, 9;
# 我们假设 用户输入 上面的信息，必定会遵守下面的规则：
#   学生信息之间用分号隔开（分号前后可能有不定数量的空格），
#   每个学生信息里的 姓名和 年龄之间用 逗号隔开（逗号前后可能有不定数量的空格）
# 2. 程序随后将输入的学生信息分行显示，格式如下
# Jack Green :   21;
# Mike Mos   :   09;
# 学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零

# 1.用户输入信息
#   1.1 message = input
# 2.提取用户信息
#   2.1 message.split（‘；’），分完是个list['jack,21','mike,9'...]  叫msg2 ,注意最后一个空字符！！！！！
# 3.提取单个用户信息
#   3.1 取出每个单个用户的信息并按逗号分开获取变量,这里考虑用户信息空格的问题
#        for one in msg2:
#            two = one.split(',')
# 4.分别提取单个用户的姓名和年龄
#         name = two[0]
#         age = two[1]
#         name = name.strip()
#         age = age.strip()
# 5.打印出来，按要求的格式
#      print(f'{name:20} : {age:02}')

msg = input('请输入信息： ')
msg2 = msg.split(';')
for one in msg2:
    if one == '':
        continue
    name,age = one.split(',')
    name = name.strip()
    age = age.strip()
    age = int(age)
    print(f'{name:20} : {age:02}')




