# 请定义一个函数 mySort，参数为一个列表，参数列表中的元素都是整数.
# mySort 函数需要将参数列表中的元素按从小到大排序，最终返回一个新的list。
#
# 请按下面算法的思路实现函数：
#
# 1. 创建一个新的列表newList
# 2. 先找出所有元素中最小的，append在newList里面
# 3. 再找出剩余的所有元素中最小的，append在newList里面
# 4. 依次类推，直到所有的元素都放到newList里面

newList = []
def mySort(X):
    while len(X) > 0:
        minx = min(X)
        newList.append(minx)
        X.remove(minx)
    return newList
print(mySort([3,2,1,4,6,7,19,13,21]))
