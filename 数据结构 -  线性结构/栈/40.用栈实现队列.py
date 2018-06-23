"""
40. 用栈实现队列
正如标题所述，你需要使用两个栈来实现队列的一些操作。

队列应支持push(element)，pop() 和 top()，其中pop是弹出队列中的第一个(最前面的)元素。

pop和top方法都应该返回第一个元素的值。

样例
比如push(1), pop(), push(2), push(3), top(), pop()，你应该返回1，2和2

挑战
仅使用两个栈来实现它，不使用任何其他数据结构，push，pop 和 top的复杂度都应该是均摊O(1)的
"""

# time: 964 ms
class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        # write your code here
        self.stack2.append(element)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        a = self.stack2[0]
        self.stack2.remove(self.stack2[0])
        return a

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        a = self.stack2[0]
        return a
q = MyQueue()
q.push(1)
print(q.pop())
q.push(2)
q.push(3)
print(q.top())
print(q.pop())
