# 现有文件1（如下，请保存到文件file1.txt中）， 记录了公司员工的薪资，其内容格式如下
#
# name: Jack   ;    salary:  12000
#  name :Mike ; salary:  12300
# name: Luk ;   salary:  10030
#   name :Tim ;  salary:   9000
# name: John ;    salary:  12000
# name: Lisa ;    salary:   11000
#
# 每个员工一行，记录了员工的姓名和薪资，
# 每行记录 原始文件中并不对齐，中间有或多或少的空格
#
# 现要求实现一个python程序，计算出所有员工的税后工资（薪资的90%）和扣税明细，
# 以如下格式存入新的文件 file2.txt中，如下所示
#
# name: Jack   ;    salary:  12000 ;  tax: 1200 ; income:  10800
# name: Mike   ;    salary:  12300 ;  tax: 1230 ; income:  11070
# name: Luk    ;    salary:  10030 ;  tax: 1003 ; income:   9027
# name: Tim    ;    salary:   9000 ;  tax:  900 ; income:   8100
# name: John   ;    salary:  12000 ;  tax: 1200 ; income:  10800
# name: Lisa   ;    salary:  11000 ;  tax: 1100 ; income:   9900
#
# 要求像上面一样的对齐
# tax 表示扣税金额和 income表示实际收入。注意扣税金额和 实际收入要取整数
#
# 思路：
# 1.将文件1打开，获取数据
# 2.计算需要计算的数据
# 3.将数据按固定格式展示
# 4.保存，取新名字文件2

file1 = open(r'e:\file1.txt')
file2 = open(r'e:/file2.txt','w')
for lines in file1:
    msg = lines.split(';')
    oname, osalary = msg[:2]
    oname = oname.strip()
    osalary = osalary.strip()

    msg2 = oname.split(':')
    xname, name = msg2[:2]
    xname = xname.strip()
    name = name.strip()

    msg3 = osalary.split(':')
    xsalary,salary = msg3[:2]
    xsalary = xsalary.strip()
    salary = salary.strip()

    tax = int(salary) * 0.1
    tax = int(tax)

    income = int(salary)-tax
    income = int(income)
    r = f'{xname:4}: {name:5}   ;{xsalary:10}:  {salary:>5} ;   tax: {tax:>5} ; income: {income:>5}'
    print(r)
    file2.write(r + '\n')
file1.close()
file2.close()



