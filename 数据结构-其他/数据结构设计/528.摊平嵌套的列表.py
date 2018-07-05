"""
528. 摊平嵌套的列表
给你一个嵌套的列表，实现一个迭代器将其摊平。
一个列表的每个元素可能是整数或者一个列表。

样例
给出列表 [[1,1],2,[1,1]]，经过迭代器之后返回 [1,1,2,1,1]。

给出列表 [1,[4,[6]]]，经过迭代器之后返回 [1,4,6]。
"""
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


# 思路：从前往后把对象压入栈，在倒序，这个取出来的时候，就是后进先出了
# 取出来的对象：如果是整数，返回True,如果不是整数，则遍历这个对象.直到取出来的是整数
# time:2666 ms
class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.stack = nestedList[::-1]

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        return self.stack.pop().getInteger()

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:len(self.stack) - 1] + top.getList()[::-1]
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
