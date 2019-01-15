#    签到时间              课程id  学生id
# ('2017-03-13 11:50:09',   271,   131),
# ('2017-03-14 10:52:19',   273,   131),
# ('2017-03-13 11:50:19',   271,   126),
# 参数fileName 为 数据库记录文件路径， 输出结果是将数据库记录文件中的学生签到信息保存在一个字典对象中，并作为返回值返回。
#  def putInfoToDict(fileName):
# {
#     131: [
#         {'lessonid': 271, 'checkintime': '2017-03-13 11:50:09'},
#         {'lessonid': 273, 'checkintime': '2017-03-14 10:52:19'},
#     ],
#
#     126: [
#         {'lessonid': 271, 'checkintime': '2017-03-13 11:50:19'},
#     ],
# }

# FileName = 'e:/file001.txt'

def putInfoToDict(fileName):
    InfoDict = {}
    with open(r'e:/file001.txt') as f:
        msg = f.read().splitlines()
        for msgInfo in msg:
            usefulInfo = msgInfo.replace('(', '').replace(')', '').replace(';', '').strip()
            parts = usefulInfo.split(',')

            Sid = int(parts[2].strip())
            Cid = int(parts[1].strip())
            Stime = parts[0].strip().replace("'", '')

            info2 = {'lessonid': Cid, 'checkintime': Stime}

            if Sid not in InfoDict:
                InfoDict[Sid] = []
            InfoDict[Sid].append(info2)
    return InfoDict

ret = putInfoToDict('file001.txt')
import pprint
pprint.pprint(ret)

#1.usefulInfo = msgInfo.replace('(', '').replace(')', '').replace(';', '').strip()这段之前写的是：usefulInfo = msgInfo[1:-3],
# 试图去除（）以及换行，最后显示第一个数据出来id为5，才发现最后一行没有换行符了，把id号36的6去掉了，导致数据不对了
#2.学习了splitlines()以及pprint的用法，复习了replace()用法
