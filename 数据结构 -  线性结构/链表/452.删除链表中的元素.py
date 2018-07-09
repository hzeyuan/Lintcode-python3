"""
452. 删除链表中的元素
删除链表中等于给定值val的所有节点。

样例
给出链表 1->2->3->3->4->5->3, 和 val = 3, 你需要返回删除3之后的链表：1->2->4->5。
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    # time: 1052 ms
    def removeElements(self, head, val):
        # write your code here
        p = ListNode(-float('inf'), head)
        tmp = p
        while tmp.next:
            if tmp.next.val == val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return p.next
