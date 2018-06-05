"""
用插入排序对链表排序

样例
Given 1->3->2->0->null, return 0->1->2->3->null
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """

    def insertionSortList(self, head):
        # write your code here
        if head is None: return None
        if head.next is None: return head

        new = ListNode(0)
        while head is not None:
            node = new
            fol = head.next
            while node.next is not None and node.next.val < head.val:
                node = node.next
            head.next = node.next
            node.next = head
            head = fol
        return new.next
