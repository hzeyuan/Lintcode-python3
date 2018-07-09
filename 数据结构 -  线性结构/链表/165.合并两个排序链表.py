"""
165. 合并两个排序链表
将两个排序链表合并为一个新的排序链表

样例
给出 1->3->8->11->15->null，2->null， 返回 1->2->3->8->11->15->null。
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    # 思路：两两比较然后合并到另一个新的链表上，在将多余的上于的长度添加到新的链表上
    # time:9205 ms
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if not l2:
            return l1
        elif not l1:
            return l2
        d = ListNode(0)
        tmp = d
        while l1 and l2:
            if l1.val <l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        tmp.next = l1 if l1 else l2
        return d.next


