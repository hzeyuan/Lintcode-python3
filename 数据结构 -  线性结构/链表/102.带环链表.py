"""
102. 带环链表
给定一个链表，判断它是否有环。

样例
给出 -21->10->4->5, tail connects to node index 1，返回 true

挑战
不要使用额外的空间
"""


# Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """

    # 设置两个指针，p1:每次走一步，p2:每次走两步
    # 若无环，p2会为空，若有环，最终p2会再一次超越p1一圈，及p1.val==p2.val
    # time:1568 ms
    def hasCycle(self, head):
        # write your code here
        p1 = ListNode(-1, head)
        p2 = ListNode(-2, head)
        while p2:
            if p1.val == p2.val:
                return True
            if not p2.next or not p2.next.next:
                return False
            p1 = p1.next
            p2 = p2.next.next
