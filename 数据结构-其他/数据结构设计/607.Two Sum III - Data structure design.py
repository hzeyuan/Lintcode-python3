"""
607. Two Sum III - Data structure design
设计b并实现一个 TwoSum 类。他需要支持以下操作:add 和 find。
add -把这个数添加到内部的数据结构。
find -是否存在任意一对数字之和等于这个值

样例
add(1);add(3);add(5);
find(4)//返回true
find(7)//返回false
"""

# time:643ms
class TwoSum:
    """
    @param: number: An integer
    @return: nothing
    """

    def __init__(self):
        self.res = {}

    def add(self, number):
        # write your code here
        if number not in self.res:
            self.res[number] = 1
        else:
            self.res[number] += 1

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        for i in self.res:
            if value - i == i:
                if self.res[i] >= 2:
                    return True
            else:
                if value - i in self.res:
                    return True
        return False


s = TwoSum()
s.add(1)
s.add(3)
s.add(5)
print(s.find(4))
print(s.find(7))
