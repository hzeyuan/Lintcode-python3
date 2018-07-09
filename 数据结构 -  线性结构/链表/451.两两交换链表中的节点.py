"""
451. 两两交换链表中的节点
给一个链表，两两交换其中的节点，然后返回交换后的链表。

样例
给出 1->2->3->4, 你应该返回的链表是 2->1->4->3。

挑战
你的算法只能使用常数的额外空间，并且不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    # time:944 ms
    def swapPairs(self, head):
        # Write your code here
        if head is None or head.next is None:
            return head
        dummy = ListNode(0, head)
        p = dummy
        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next
        return dummy.next


a1 = ListNode(1)
a2 = ListNode(2, a1)
a3 = ListNode(3, a2)
a4 = ListNode(4, a3)
s =Solution()
print(s.swapPairs(a4))