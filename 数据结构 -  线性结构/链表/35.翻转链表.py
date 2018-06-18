"""
35. 翻转链表
翻转一个链表

样例
给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null

挑战
在原地一次翻转完成
"""


# Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: n
    @return: The new head of reversed linked ist.
    """
    # time:588ms
    def reverse(self, head):
        curt = None
        while head:
            # 下一个节点
            temp = head.next
            # 截出head的第一个结点指向curt
            head.next = curt
            curt = head
            # head长度减1，重复这个过程
            head = temp
        return curt


a3 = ListNode(0)
a2 = ListNode(1, a3)
a1 = ListNode(2, a2)
s = Solution()
print(s.reverse(a1))