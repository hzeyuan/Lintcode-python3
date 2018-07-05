"""
657. Insert Delete GetRandom O(1)
设计一个数据结构实现在平均 O(1) 的复杂度下执行以下所有的操作。

insert(val): 如果这个元素不在set中，则插入。

remove(val): 如果这个元素在set中，则从set中移除。

getRandom: 随机从set中返回一个元素。每一个元素返回的可能性必须相同。

样例
// 初始化空集set
RandomizedSet randomSet = new RandomizedSet();

// 1插入set中。返回正确因为1被成功插入
randomSet.insert(1);

// 返回错误因为2不在set中
randomSet.remove(2);

// 2插入set中，返回正确，set现在有[1,2]。
randomSet.insert(2);

// getRandom 应该随机的返回1或2。
randomSet.getRandom();

// 从set中移除1，返回正确。set现在有[2]。
randomSet.remove(1);

// 2已经在set中，返回错误。
randomSet.insert(2);

// 因为2是set中唯一的数字，所以getRandom总是返回2。
randomSet.getRandom();
"""


# time:1007 ms
class RandomizedSet:

    def __init__(self):

        # do intialization if necessary
        self.s = set()

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """

    def insert(self, val):

        # write your code here
        if val in self.s:
            return False
        else:
            self.s.add(val)
            return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """

    def remove(self, val):
        if val not in self.s:
            return False
        else:
            self.s.remove(val)
            return True

    # write your code here

    """
    @return: Get a random element from the set
    """

    def getRandom(self):
        # write your code here
        import random
        r = random.randint(0, len(self.s))
        index = 0
        for i in self.s:
            if index == r:
                return i
            index += 1

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
