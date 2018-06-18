"""
96. 链表划分
给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。

你应该保留两部分内链表节点原有的相对顺序。



样例
给定链表 1->4->3->2->5->2->null，并且 x=3

返回 1->2->2->4->3->5->null
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """

    def partition(self, head, x):
        # write your code here
        if head is None:
            return head
        aHead, bHead = ListNode(0), ListNode(0)
        aTail, bTail = aHead, bHead
        while head:
            if head.val < x:
                aTail.next = head
                aTail = aTail.next
            else:
                bTail.next = head
                bTail = bTail.next  
            head = head.next
        bTail.next = None
        aTail.next = bHead.next
        return aHead.next


s = Solution()
a = ListNode(5)
a1 = ListNode(1, a)
print(s.partition(a1, 3))
