"""
822. 相反的顺序存储
给出一个链表，并将链表的值以in reverse order存储到数组中。

样例
给定1 -> 2 -> 3 -> null，返回[3,2,1]。
"""


class Solution:
    """
    @param head: the given linked list
    @return: the array that store the values in reverse order
    """

    # time: 1223ms
    def reverseStore(self, head):
        # write your code here
        res = []
        while head:
            res.insert(0, head.val)
            head = head.next
        return res
